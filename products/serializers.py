from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # orders = serializers.HyperlinkedRelatedField(many=True,
                                                #    read_only=True,
                                                #    view_name="order-detail")

    # orders = OrderSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id','product_name', 'description', 'category', 'image_url', 'price', 'stock_quantity',)