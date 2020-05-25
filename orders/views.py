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
        print("request data:")
        print(request.data)
#
        if serializer.is_valid():
            serializer.save()
            get_line_product_price = ProductPrice.objects.filter(order_id = serializer.data["id"]).first()
            print(f"this is the table product price: {get_line_product_price}")
            # price_update = Product.objects.filter(pk = request.data["products"][0])["price"]
            for product_id in request.data["products"]:
                print(product_id)
                product = Product.objects.filter(pk=product_id).first()
                product_price = product.price
                print(product_price)
            updated_line = ProductPrice.objects.filter(order_id = serializer.data["id"]).update(ordered_price = product_price)

            
            # order_id = serializer.data["id"]
            # for product_id in request.data['products']:
            #     product_price = Product.objects.get(pk=product_id).price
            #     data_for_serializer = {'product': product_id, 'ordered_price': product_price, 'order': order_id}
            #     M2M_Serializer = ProductPriceSerializer(data = data_for_serializer)
            #     print(M2M_Serializer)
            #     if M2M_Serializer.is_valid():
            #         print("IS IT IN IS VALID?")
            #         M2M_Serializer.save()
            #         return Response(M2M_Serializer.data, status=status.HTTP_201_CREATED)
            #     return Response(M2M_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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