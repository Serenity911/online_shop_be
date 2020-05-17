from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Product()._meta.get_field('id'))

    class Meta:
        model = Product
        fields = ('id','product_name', 'description', 'category', 'image_url', 'price', 'stock_quantity',)