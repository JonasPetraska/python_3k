from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
