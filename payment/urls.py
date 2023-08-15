from django.urls import path
from . import views

urlpatterns = [
    path('payments/create/', views.create_payment, name='create_payment'),
    path('payments/edit/<int:pk>/', views.edit_payment, name='edit_payment'),
    path('payments/list/', views.payment_list, name='payment_list'),
    path('payments/detail/<int:pk>/', views.payment_detail, name='payment_detail'),


]
