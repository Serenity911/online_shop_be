from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .serializers import OrderSerializer, ProductPriceSerializer

from .models import Order, ProductPrice
from products.models import Product
from products.views import *

class OrderListCreateAPIView(APIView):
    def get(self,request):
        orders = Order.objects.all()
        # orders = Order.objects.filter(active=True)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)

#
        if serializer.is_valid():
            serializer.save()
            get_order_product_price = ProductPrice.objects.filter(order_id = serializer.data["id"]).first()
            for product_id in request.data["products"]:
                product = Product.objects.filter(pk=product_id).first()
                product_price = product.price
                get_order_product = ProductPrice.objects.filter(order_id = serializer.data["id"], product_id = product_id)
                updated_line = ProductPrice.objects.filter(order_id = serializer.data["id"], product_id = product_id).update(ordered_price = product_price)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailAPIView(APIView):
    def get_object(self, pk):
        order = get_object_or_404(Order, pk=pk)
        return order

    def get(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)