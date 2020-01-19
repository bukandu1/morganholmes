from django.db import models

# Create your models here.

#Investors
#Payments

class Investor(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
