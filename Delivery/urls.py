from django.urls import path
from . import views

app_name = 'delivery'

urlpatterns = [
    path('create/', views.create_delivery, name='create_delivery'),
    path('<int:pk>/edit/', views.edit_delivery, name='edit_delivery'),
    path('<int:pk>/', views.delivery_detail, name='detail_delivery'),
    path('list/', views.delivery_list, name='list_delivery'),
]
