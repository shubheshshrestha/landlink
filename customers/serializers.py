from rest_framework import serializers
from customers.models import CustomerProfile

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['id', 'user', 'shipping_address', 'billing_address', 'phone_number']
        read_only_fields = ['user']