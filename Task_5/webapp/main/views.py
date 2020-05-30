from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from .models import Form, FormLine

# Create your views here.

@login_required
def home(request):
    forms = Form.objects.filter(main_member=request.user)
    return render(request, 'main/home.html', {'forms': forms});

class CreateForm(CreateView):
    model = Form
    template_name = 'main/form/create.html'
    fields = ['company_title', 'act_nr', 'location', 'creditor_name', 'invoice_series', 'invoice_number', 'responsible_member', 'member1', 'member2', 'member3', 'member4']

    #set main member by default as current user
    def form_valid(self, form):
        form.instance.main_member = self.request.user
        return super().form_valid(form)

class FormDetails(LoginRequiredMixin, DetailView):
    model = Form
    template_name = "main/form/detail.html"
    def get_context_data(self, **kwargs):
        context = super(FormDetails, self).get_context_data(**kwargs)
        form = Form.objects.get(pk=self.kwargs['pk'])
        
        #get lines
        context['lines'] = form.formline_set.all()

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