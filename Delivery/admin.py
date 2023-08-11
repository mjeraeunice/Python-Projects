from django.contrib import admin
from.models import Delivery
# Register your models here.
class DeliveryAdmin(admin.ModelAdmin):
    display_list=('name','address','phone_number','distance')
admin.site.register(Delivery,DeliveryAdmin)