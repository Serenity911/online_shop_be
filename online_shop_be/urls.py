"""online_shop_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products.views import *
from orders.views import * 

# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'products', viewProducts.ProductView, 'product')
# router.register(r'orders', viewOrders.OrderView, 'order')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls))
# ]
urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/orders/", 
         OrderListCreateAPIView.as_view(), 
         name="order-list"),

    path("api/orders/<int:pk>/", 
         OrderDetailAPIView.as_view(), 
         name="order-detail"),

    path("api/products/", 
         ProductListCreateAPIView.as_view(), 
         name="product-list"),
         
    path("api/products/<int:pk>", 
         ProductListCreateAPIView.as_view(), 
         name="product-detail")
]