from django.contrib import admin
from .models import *
from orders.admin import ProductPriceInline
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductPriceInline,)

admin.site.register(Product, ProductAdmin)
