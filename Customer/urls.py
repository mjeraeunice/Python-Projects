
from django.urls import path
from . import views

urlpatterns = [
    path('customer/add/', views.add_customer, name='add_customer'),
    path('customer/edit/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('customer/list/', views.customer_list, name='customer_list'),
    path('customer/detail/<int:customer_id>/', views.customer_detail, name='customer_detail'),
]
