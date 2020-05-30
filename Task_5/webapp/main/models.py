from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Form(models.Model):
    company_title = models.CharField(max_length=100)
    act_nr = models.CharField(max_length=100)
    act_date = models.DateTimeField(auto_now_add=True, blank=True)
    approved_date = models.DateTimeField(auto_now_add=True, blank=True)
    main_member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='main_member', blank=True)
    member1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member1')
    member2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member2', blank=True, null=True)
    member3 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member3', blank=True, null=True)
    member4 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member4', blank=True, null=True)
    location = models.CharField(max_length=100)
    creditor_name = models.CharField(max_length=100)
    invoice_series = models.CharField(max_length=10)
    invoice_number = models.CharField(max_length=100)
    invoice_date = models.DateTimeField(auto_now_add=True, blank=True)
    responsible_member = models.CharField(max_length=100)

    #redirect url
    #def get_absolute_url(self):
    #    return reverse('form-details', kwargs={'pk': self.pk})
