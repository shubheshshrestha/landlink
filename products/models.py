from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
class Product(models.Model):
    supplier = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
        