from django.db import models
from inventory.models import Product
from django.contrib.auth.models import User

# Create your models here.
class MyCart(models.Model):
    product_name = models.CharField(max_length=32)
    product_quantity = models.IntegerField()
    product_price = models.IntegerField()
    product_avatar = models.ImageField()
    date_added = models.DateTimeField()
    products = models.ManyToManyField(Product)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = "My cart"