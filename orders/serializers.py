from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer, Product
# from customers.serializers import CustomerProfileSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='product', read_only=True) # Include product details using ProductSerializer

    class Meta:
        model = OrderItem
        # Fields to include in the serialization 
        fields = ['id', 'product', 'product_details', 'quantity', 'price', 'subtotal']
        # Fields that should be read-only
        read_only_fields = ['price', 'subtotal']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True) # Include order items 
    customer_details = serializers.SerializerMethodField() # Method field to include customer details

    class Meta:
        model = Order                                                            
        fields = ['id', 'customer', 'customer_details', 'items', 'total_price', 'status', 'created_at', 'updated_at']   # Fields to include in the serialization
        read_only_fields = ['customer', 'total_price', 'status', 'created_at', 'updated_at']    # Fields that should be read-only

        def get_customer_details(self, obj):    # Method to add customer details to the serialization
            return {
                'id': obj.customer.id,
                'username': obj.customer.username,
                'email': obj.customer.email
            }

        # Custom create method to handle nested items data
        def create(self, validated_data):
            customer = self.context['request'].user # Get the current user
            order = Order.objects.create(customer=customer, **validated_data)   # Create the order

            # Process each item from the requested data
            items_data = self.context['request'].data.get('items', [])
            for item_data in items_data:
                product = Product.objects.get(id=items_data['product'])
                OrderItem.objects.create(
                    order = order,
                    product = product,
                    quantity = item_data['quantity']
                )
                
            # Save the order to trigger total price calculation     
            order.save() 
            return order
# class OrderSerializer(serializers.ModelSerializer):
#     # Include related data for read operations
#     product_details = ProductSerializer(source='product', read_only=True)
#     customer_details = CustomerProfileSerializer(source='customer', read_only=True)
#     class Meta:
#         model = Order
#         fields = ['id', 'customer', 'product', 'quantity', 'total_price', 'status', 'created_at', 'updated_at']

#         # These fields should be automatically handled by the system
#         read_only_fields = ['total_price', 'created_at', 'updated_at']