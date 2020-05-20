from rest_framework import serializers
from .models import Order, ProductPrice
from products.models import Product


class ProductPriceSerializer(serializers.ModelSerializer):
    product = serializers.HyperlinkedRelatedField(many=True,
                                                   read_only=True,
                                                   view_name="product-detail")
    order = serializers.HyperlinkedRelatedField(many=True,
                                                   read_only=True,
                                                   view_name="order-detail")
    ordered_price = 1

    class Meta:
        model = ProductPrice
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = Order
        exclude = ('id',)
    
    # def validate(self, data):
    #     # products not empty
    #     pass







# class OrderSerializer(serializers.ModelSerializer):
#     products = serializers.PrimaryKeyRelatedField(many = True, read_only=True)
#     class Meta:
#         model = Order
#         fields = ('id','order_date','products','delivery_address','delivery_postcode')
