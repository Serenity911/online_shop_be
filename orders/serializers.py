from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many = True, read_only=True)
    class Meta:
        model = Order
        fields = ('id','order_date','products','delivery_address','delivery_postcode')
