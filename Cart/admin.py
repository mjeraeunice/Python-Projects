from django.contrib import admin
from .models import MyCart

# Register your models here.
class MyCartAdmin(admin.ModelAdmin):
    list_display = ("product_name","product_quantity","product_price", "product_avatar","date_added",)
admin.site.register(MyCart,MyCartAdmin)