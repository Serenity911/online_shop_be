from django.contrib import admin
from .models import *
# Register your models here.
class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = (ProductPriceInline,)

admin.site.register(Order, OrderAdmin)

