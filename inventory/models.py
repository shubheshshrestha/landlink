from django.db import models
from products.models import Product

# Create your models here.

class InventoryLog(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    action = models.CharField(max_length=20) # 'increase' or 'decrease'
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} ({self.action})"