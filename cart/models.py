from django.db import models
from inventory.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    items_name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    number_of_items = models.PositiveIntegerField(default=1)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s Cart: {self.items_name}"
    
    class Meta:
        verbose_name_plural = "cart"