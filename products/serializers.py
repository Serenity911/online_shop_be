from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id','product_name', 'description', 'category', 'image_url', 'price', 'stock_quantity',)