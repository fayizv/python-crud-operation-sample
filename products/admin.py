from itertools import product
from django.contrib import admin
from . models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stoke')


# Register your models here.
admin.site.register(Product)