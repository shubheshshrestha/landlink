from django.db import models
from products.models import Product
from orders.models import Order

# Create your models here.

class SalesReport(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_units = models.IntegerField()
    report_date = models.DateField(auto_now=True)

    