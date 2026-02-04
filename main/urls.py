from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('product/<int:id>/', product_detail, name='product_detail'),
]
