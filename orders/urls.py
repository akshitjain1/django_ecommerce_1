from django.urls import path
from .views import *
urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('update/<int:product_id>/<str:action>/', update_cart, name='update_cart'),
    path('place-order/', place_order, name='place_order'),
    path('success/', order_success, name='order_success'),
]
