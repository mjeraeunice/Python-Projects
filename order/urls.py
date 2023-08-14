# order/urls.py
from django.urls import path
from .views import create_order 
from.views import edit_order
from.views import order_list
from.views import order_detail

urlpatterns = [
    path("orders/create/", create_order, name="create_order"),
    path("orders/edit/<str:order_number>/",edit_order, name="edit_order"),
    path("orders/list/",order_list, name="order_list"),
    path("orders/detail/<str:order_number>/",order_detail, name="order_detail"),
]
