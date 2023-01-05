import email
from email.mime import image
from pickle import TRUE
from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    spech = models.CharField(max_length=255)
    price  = models.FloatField()
    offer_price =models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2000)



