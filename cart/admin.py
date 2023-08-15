from django.contrib import admin
from.models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display=("user","product","items_name","price","number_of_items","discount","quantity","description")
admin.site.register(Cart,CartAdmin)