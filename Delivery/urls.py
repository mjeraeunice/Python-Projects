from django.urls import path
from . import views

app_name = 'delivery'

urlpatterns = [
    path('delivery/create/', views.create_delivery, name='create_delivery'),
    path('delivery/<int:pk>/edit/', views.edit_delivery, name='edit_delivery'),
    path('delivery/<int:pk>/', views.delivery_detail, name='delivery_detail'),
    path('delivery/list/', views.delivery_list, name='delivery_list'),
]
