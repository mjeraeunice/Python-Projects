from django.contrib import admin
from.models import Token
# Register your models here.
class CustomerServiceAdmin(admin.ModelAdmin):
    list_display = ("email", "phone_number", "customer_name", "date_created", "date_updated")
admin.site.register(Token, CustomerServiceAdmin)