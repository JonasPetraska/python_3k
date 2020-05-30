from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Form(models.Model):
    company_title = models.CharField(max_length=100)
    act_nr = models.CharField(max_length=100)
    act_date = models.DateTimeField(auto_now_add=True, blank=True)
    approved_date = models.DateTimeField(auto_now_add=True, blank=True)
    main_member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commissioner', blank=True)
    member1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commissioner1')
    member1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commissioner2', blank=True)
    member1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commissioner3', blank=True)
    member1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commissioner4', blank=True)
    location = models.CharField(max_length=100)
    creditor_name = models.CharField(max_length=100)
    invoice_series = models.CharField(max_length=10)
    invoice_number = models.CharField(max_length=100)
    invoice_date = models.DateTimeField(auto_now_add=True, blank=True)
    responsible_member = models.CharField(max_length=100)
