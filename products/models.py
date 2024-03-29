from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.TextField(null=False)
    description = models.TextField(null=False)
    image_url = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock_quantity = models.IntegerField()

