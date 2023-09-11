from django.urls import path
from . import views

urlpatterns = [
    path('view-cart/', views.view_cart, name='view_cart'),
    path('update-cart/<int:id>/', views.update_cart, name='update_cart'),
    path('remove-item/<int:id>/', views.remove_item, name='remove_item'),
    path('empty-cart/', views.empty_cart, name='empty_cart'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
]

