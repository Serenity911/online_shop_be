from rest_framework import serializers
from .models import Order, ProductPrice
from products.models import Product


class ProductPriceSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.product_id')
    order = serializers.ReadOnlyField(source='order.order_id')

    ordered_price = serializers.DecimalField(max_digits=5, decimal_places=2)


    class Meta:
        model = ProductPrice
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())


    class Meta:
        model = Order
        fields ="__all__"
