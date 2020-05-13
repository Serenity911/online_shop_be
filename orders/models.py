from django.db import models
import customers.models as customers
import products.models as products

# Create your models here.
class Order(models.Model):
    order_date = models.DateField(auto_now_add = True)
    # customer = models.ForeignKey(customers.Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(products.Product, related_name='orders', through='Product_Price')
    delivery_address = models.CharField(max_length=200)
    delivery_postcode = models.CharField(max_length=7)

    def __str__(self):
        return self.delivery_address


class Product_Price(models.Model):
    product = models.ForeignKey(products.Product, related_name='product_price', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='product_price', on_delete=models.CASCADE)
    # def product_price:
    #     return product.objects.get()

    ordered_price = models.DecimalField(default='1.00', max_digits=5, decimal_places=2, editable=False)
