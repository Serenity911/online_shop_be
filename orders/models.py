from django.db import models
import customers.models as customers
import products.models as products
# from django.contrib import admin

# Create your models here.
class Order(models.Model):
    order_date = models.DateField(auto_now_add = True)
    # customer = models.ForeignKey(customers.Customer, on_delete=models.CASCADE)
    # products = models.ManyToManyField(products.Product,related_name = "orders")
    # CHECK: adding the through makes the M2M explicit, and the field product on orders disappears
    products = models.ManyToManyField(products.Product,related_name = "orders", through='ProductPrice')
    delivery_address = models.CharField(max_length=200)
    delivery_postcode = models.CharField(max_length=7)

    def __str__(self):
        return self.delivery_address

class ProductPrice(models.Model):
    product = models.ForeignKey(products.Product, related_name='product_price', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='product_price', on_delete=models.CASCADE)
    ordered_price = models.DecimalField(max_digits=5, decimal_places=2, null = True)

