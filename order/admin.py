from django.contrib import admin
from.models import Order
# Register your models here.
class OderAdmin(admin.ModelAdmin):
    list_display =('order_number','customer_name','customer_email','customer_phone_number','order_date','order_status')
admin.site.register(Order,OderAdmin)