from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image_url = models.CharField(max_length=255)
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    slug = AutoSlugField(populate_from=lambda instance: instance.product_name,
                         slugify=lambda value: value.replace(' ','-'))

    def __str__(self):
        return self.product_name