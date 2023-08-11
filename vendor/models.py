from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Vendor"