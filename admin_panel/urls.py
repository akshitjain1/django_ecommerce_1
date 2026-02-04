from django.urls import path
from .views import *
urlpatterns = [
    path('admin-panel/login/', admin_login, name='admin_login'),
    path('admin-panel/', admin_dashboard, name='admin_dashboard'),

    path('admin-panel/products/', admin_products, name='admin_products'),
    path('admin-panel/products/add/', admin_add_product, name='admin_add_product'),
    path('admin-panel/products/edit/<int:id>/', admin_edit_product, name='admin_edit_product'),
    path('admin-panel/products/delete/<int:id>/', admin_delete_product, name='admin_delete_product'),

    path('admin-panel/orders/', admin_orders, name='admin_orders'),
    path('admin-panel/orders/<int:id>/', admin_order_detail, name='admin_order_detail'),
]
