from django.urls import path
from.views import product_upload_view
from.views import products_list_view
from.views import product_detail_view
from.views import edit_product_view

urlpatterns=[
    path("products/upload/",product_upload_view,name="product_upload_view"),
    path("products/list/",products_list_view,name="products_list_view"),
    path("products/<int:id>/",product_detail_view,name="product_detail_view"),
    path("products/edit/<int:id>/",edit_product_view,name="product_edit_view")
]