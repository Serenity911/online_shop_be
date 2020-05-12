from django.db import models
import customers.models as customers
import products.models as products

# Create your models here.
class Order(models.Model):
    order_date = models.DateField(auto_now_add = True)
    # customer = models.ForeignKey(customers.Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(products.Product)
    delivery_address = models.CharField(max_length=200)
    delivery_postcode = models.CharField(max_length=7)

    def __str__(self):
        return self.delivery_address