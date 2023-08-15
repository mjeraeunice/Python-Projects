from django.urls import path
from . import views

urlpatterns = [
    path('reviews/create/', views.create_review, name='create_review'),
    path('reviews/edit/<int:pk>/', views.edit_review, name='edit_review'),
    path('reviews/list/', views.review_list, name='review_list'),
    path('reviews/detail/<int:pk>/', views.review_detail, name='review_detail'),
]
