from django.shortcuts import render

from rest_framework import viewsets          # add this
from .serializers import ProductSerializer      # add this
from .models import Product             # add this
# Create your views here.

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()