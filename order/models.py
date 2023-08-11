from django.db import models
from Cart.models import MyCart
from Customer.models import Customer
from Delivery.models import Delivery
# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=32, unique=True)
    customer_name = models.CharField(max_length=32)
    customer_email = models.EmailField(max_length=255)
    customer_phone_number = models.CharField(max_length=15)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=16, choices=[
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ])
    customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    cart=models.OneToOneField(MyCart,null=True,on_delete=models.CASCADE)
    delivery=models.ForeignKey(Delivery,null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Order"

