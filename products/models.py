from django.db import models
from autoslug import AutoSlugField

# Create your models here.

def get_populate_from(instance):
    return '%s-%s' % (instance.product_name)
    
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image_url = models.CharField(max_length=255)
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    slug = AutoSlugField(populate_from=get_populate_from)

    def __str__(self):
        return self.product_name
