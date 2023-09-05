from django.urls import path
from .views import product_upload_view
from .views import products_list
from .views import product_detail
from .views import product_update_view
from .views import delete_product
from django.conf import settings
from django.conf.urls.static  import static

urlpatterns = [
    path('products/upload',product_upload_view, name='product_upload_view'),
    path("products/list", products_list, name="products_list"),
    path("product/<int:id>/", product_detail, name="product_detail"),
    path("product/edit/<int:id>/", product_update_view, name="product_update_view"),
    path("product/delete/<int:id>/", delete_product , name="delete_product"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)