from rest_framework import serializers
from .models import Order, ProductPrice
from products.models import Product


class ProductPriceSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.product_id')
    order = serializers.ReadOnlyField(source='order.order_id')
    # ordered_price = serializers.ReadOnlyField(source='product.price')

    # product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    # order = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())
    ordered_price = serializers.DecimalField(max_digits=5, decimal_places=2)
#     # product = serializers.HyperlinkedRelatedField(many=True,
#     #                                                read_only=True,
#     #                                                view_name="product-detail")
#     # order = serializers.HyperlinkedRelatedField(many=True,
#     #                                                read_only=True,
#     #                                                view_name="order-detail")
    # def create(self, validated_data):
    #     print("***********IS IT GETTING HERE*******")
    #     print(validated_data)
    #     return ProductPrice.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.product = validated_data.get('product', instance.product)
    #     instance.order = validated_data.get('order', instance.order)
    #     instance.ordered_price = 111
    #     instance.save()
    #     return instance

    class Meta:
        model = ProductPrice
        # exclude =('ordered_price',)
        fields = "__all__"
        # fields = ('product',)

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    # products = ProductPriceSerializer(many=True)

    # def create(self, validated_data):
    #     print("***********ORDEEER*******")
    #     print(validated_data)
    #     Order.objects.add()
    #     return Order.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     print("getting here??????????????????????????????????")
    #     instance.products = validated_data.get('products', Product.objects.filter(pk=instance.products))
    #     instance.delivery_address = validated_data.get('delivery_address', instance.delivery_address)
    #     instance.delivery_postcode = validated_data.get('delivery_postcode', instance.delivery_postcode)
    #     instance.save()
    #     return instance

    class Meta:
        model = Order
        fields ="__all__"
        # exclude = ('id',)
    
    # def validate(self, data):
    #     # products not empty
    #     pass







# class OrderSerializer(serializers.ModelSerializer):
#     products = serializers.PrimaryKeyRelatedField(many = True, read_only=True)
#     class Meta:
#         model = Order
#         fields = ('id','order_date','products','delivery_address','delivery_postcode')
