from django.db import models
from django.contrib.auth import get_user_model 
from products.models import Product

# Create your models here.

User = get_user_model()

class Order(models.Model):
    STATUS_CHOICES = {
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('returned', 'Returned')
    }
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"