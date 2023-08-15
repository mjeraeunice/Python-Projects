from django.db import models

# Create your models here.
class Payment(models.Model):
    PAYMENT_METHODS = (
        ('NB', 'Lipa na Mpesa'),
        ('PP', 'Cash')
    )
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Failed'),
    )
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHODS)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    description = models.TextField()