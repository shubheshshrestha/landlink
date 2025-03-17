from rest_framework import serializers
from .models import Order
from products.serializers import ProductSerializer
from customers.serializers import CustomerProfileSerializer

class OrderSerializer(serializers.ModelSerializer):
    # Include related data for read operations
    product_details = ProductSerializer(source='product', read_only=True)
    customer_details = CustomerProfileSerializer(source='customer', read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'customer', 'product', 'quantity', 'total_price', 'status', 'created_at', 'updated_at']

        # These fields should be automatically handled by the system
        read_only_fields = ['total_price', 'created_at', 'updated_at']