from django.contrib import admin
from.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","image","phone","email","password")
admin.site.register(Customer,CustomerAdmin)