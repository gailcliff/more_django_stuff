from django.contrib.admin import site

# Register your models here.

from .models import *

site.register(Customer)
site.register(Product)
site.register(Order)
site.register(ProductTag)
