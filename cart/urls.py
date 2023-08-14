from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('carts/list/', views.cart_list, name='cart_list'),
    path('carts/<int:pk>/', views.cart_item_detail, name='cart_item_detail'),
    path('carts/<int:pk>/edit/', views.edit_cart_item, name='edit_cart_item'),
    path('carts/<int:pk>/remove/', views.remove_cart_item, name='remove_cart_item'),
]
