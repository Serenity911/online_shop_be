from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('', views.ProductList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)