from rest_framework import serializers
from .models import *
from products.serializers import *
from products.models import *


class ProductPriceSerializer(serializers.HyperlinkedModelSerializer):
    ordered_price = serializers.ReadOnlyField(source = 'price')
    product  = serializers.ReadOnlyField(source='product_name')
    order = serializers.ReadOnlyField(source='order.id')
    class Meta:
        model = Product_Price
        fields = ('id', 'product', 'order', 'ordered_price',)


class OrderSerializer(serializers.ModelSerializer):
    products = ProductPriceSerializer(many=True, source='productprice_set')

    # def create(self, validated_data):
    #     import pdb; pdb.set_trace()

    #     print(validated_data)
    #     products_data = validated_data.pop('products')
    #     order = Order.objects.create(**validated_data)
    #     print(products_data)
    #     for product_data in products_data:
    #         ordered_price = product_data['price']
    #         # product_to_add = Product.objects.get(product_data[])
    #         # product_to_add = Product.objects.create(**product_data)
    #         print(ordered_price)
    #         something = Product_Price.objects.create(ordered_price=ordered_price, order = order, product = product_data['id'])
    #         print(something)
    #     return order

    class Meta:
        model = Order
        fields = ('id','order_date','products', 'delivery_address','delivery_postcode',)
