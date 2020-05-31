from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Form, FormLine
from django.template.loader import get_template
from io import BytesIO
from django.http import HttpResponse

# Create your views here.

@login_required
def home(request):
    forms = Form.objects.filter(main_member=request.user)
    return render(request, 'main/home.html', {'forms': forms});

def form_as_pdf(request, *args, **kwargs):
    template = get_template('pdf.html')
    data = get_form_pdf_data(kwargs)

class CreateForm(LoginRequiredMixin, CreateView):
    model = Form
    template_name = 'main/form/create.html'
    fields = ['company_title', 'act_nr', 'location', 'creditor_name', 'invoice_series', 'invoice_number', 'responsible_member', 'member1', 'member2', 'member3', 'member4']

    #set main member by default as current user
    def form_valid(self, form):
        form.instance.main_member = self.request.user
        return super().form_valid(form)

class EditForm(LoginRequiredMixin, UpdateView):
    model = Form
    template_name = 'main/form/edit.html'
    fields = ['company_title', 'act_nr', 'location', 'creditor_name', 'invoice_series', 'invoice_number', 'responsible_member', 'member1', 'member2', 'member3', 'member4']
    
    def get(self, request, *args, **kwargs):
        form = Form.objects.get(pk=self.kwargs['pk'])
        self.object = form;
        context = self.get_context_data(object=form)
        return self.render_to_response(context)

class FormDetails(LoginRequiredMixin, DetailView): 
    model = Form
    template_name = "main/form/detail.html"
    def get_context_data(self, **kwargs):
        context = super(FormDetails, self).get_context_data(**kwargs)
        form = Form.objects.get(pk=self.kwargs['pk'])
        
        #get lines
        context['lines'] = form.formline_set.all()
        total = 0;
        for line in form.formline_set.all():
            total = total + line.sum;
        context['line_total'] = total;

        return context

class ListForms(LoginRequiredMixin, ListView):
    model = Form
    template_name = 'main/home.html'
    context_object_name = 'forms'
    ordering =  ['-approved_date']

    def get_context_data(self, **kwargs):
        context = super(ListForms, self).get_context_data(**kwargs)
        context['forms'] = Form.objects.filter(main_member=self.request.user)
        return context

class CreateFormLine(LoginRequiredMixin, CreateView):
    model = FormLine
    template_name = 'main/form/line/create.html'
    fields = ['name', 'description', 'quantity', 'quantity_type', 'sum']

    #set form reference and calculate cost by sum/quantity without rounding
    def form_valid(self, form):
        form.instance.form = Form.objects.get(pk=self.kwargs['pk'])
        form.instance.cost = form.instance.sum/form.instance.quantity
        return super().form_valid(form)

def get_form_pdf_data(kwargs):
    data = Form.objects.get(pk=kwargs['pk'])
    data_tosend = vars(data)
    data_tosend['lines'] = data.formline_set.all()
    data_tosend['main_member'] = data.main_member.username if not data.main_member.first_name else data.main_member.first_name + ' ' + data.main_member.last_name
    data_tosend['member1'] = data.member1.username if not data.member1.first_name else data.member1.first_name + ' ' + data.member1.last_name
    data_tosend['member2'] = data.member2.username if not data.member2.first_name else data.member2.first_name + ' ' + data.member2.last_name
    data_tosend['member3'] = data.member3.username if not data.member3.first_name else data.member3.first_name + ' ' + data.member3.last_name
    data_tosend['member4'] = data.member4.username if not data.member4.first_name else data.member4.first_name + ' ' + data.member4.last_name
    total = 0
    for line in data.formline_set.all():
        total = total + line.sum
    data_tosend['line_total'] = total
    return data_tosend

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None