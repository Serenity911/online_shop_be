from rest_framework import serializers
from .models import *
from products.serializers import *
from products.models import *


# class ProductPriceSerializer(serializers.HyperlinkedModelSerializer):
#     ordered_price = serializers.ReadOnlyField(source = 'price')
#     product  = serializers.ReadOnlyField(source='product_name')
#     order = serializers.ReadOnlyField(source='order.id')
#     class Meta:
#         model = Product_Price
#         fields = ('id', 'product', 'order', 'ordered_price',)


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False)
    # products = ProductPriceSerializer(many=True, source='product_price_set')
    def create(self, validated_data):
        products = validated_data.pop('products', [])
        # print(validated_data)
        total_order = 20
        instance = Order.objects.create(total_order=total_order, **validated_data)
        for product_data in products:
            product = Product.objects.get(pk=product_data.get('id'))
            instance.products.add(product)
        return instance 

    def update(self, instance, validated_data):
        products = validated_data.pop('products', [])
        instance = super().update(instance, validated_data)
        for product_data in products:
            print(instance.products)

            product = Product.objects.get(pk=product_data.get('id'))
            instance.products.add(product)
            print(instance.products)
        instance.total_order = 20

        return instance 



    # def create(self, validated_data):
    # # #     import pdb; pdb.set_trace()
    #     print("************HELLO*************************")
    #     print(validated_data)
    #     products_data = validated_data.pop('products')
    #     print(products_data)
    #     total_order = validated_data.pop('total_order')
    #     print(total_order)
    #     delivery_address = validated_data.pop('delivery_address')
    #     print(delivery_address)
    #     delivery_postcode = validated_data.pop('delivery_postcode')
    #     print(delivery_postcode)
    #     new_validated_data = {"products": products_data, "total_order": total_order, "delivery_address": delivery_address, "delivery_postcode": delivery_postcode}
    #     order = Order.objects.create(**new_validated_data)
    # #     for product_data in products_data:
    # #         ordered_price = product_data['price']
    # #         # product_to_add = Product.objects.get(product_data[])
    # #         # product_to_add = Product.objects.create(**product_data)
    # #         print(ordered_price)
    # #         something = Product_Price.objects.create(ordered_price=ordered_price, order = order, product = product_data['id'])
    # #         print(something)
        # return order

    class Meta:
        model = Order
        fields = ('id','order_date','products', 'delivery_address','delivery_postcode',)
        # read_only_fields = ['total_order']
        # If you define a depth, you now have to write your own create and update methods that will handle the modification of the nested fields.
        # depth = 1
