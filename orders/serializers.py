from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer, Product

class OrderItemSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_details', 'quantity', 'price', 'subtotal']
        read_only_fields = ['price', 'subtotal']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    customer_details = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'customer_details', 'items', 'total_price', 'status', 'created_at', 'updated_at']
        read_only_fields = ['customer', 'total_price', 'created_at', 'updated_at']

    def get_customer_details(self, obj):
        return {
            'id': obj.customer.id,
            'user': {
                'id': obj.customer.user.id,
                'username': obj.customer.user.username,
                'email': obj.customer.user.email
            },
            'shipping_address': obj.customer.shipping_address,
            'billing_address': obj.customer.billing_address,
            'phone_number': obj.customer.phone_number
        }

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])  # Handle missing items gracefully.
        customer_profile = self.context['request'].user.customerprofile
        order = Order.objects.create(customer=customer_profile, **validated_data)
        # order.save() # Saving to fix the missing primary key issue

        for item_data in items_data:
            item_data['order'] = order.id 
            OrderItem.objects.create(**item_data)

        order.save()
        return order
    
            # product = Product.objects.get(id=item_data['product'])
            # quantity = item_data['quantity']
            # OrderItem.objects.create(
            #     order=order, # Use the saved order
            #     product=product,
            #     quantity=quantity,
            #     price=product.price
            # )

        # order.save() # save the order again to recalculate the total price
        # return order


# from rest_framework import serializers
# from .models import Order, OrderItem
# from products.serializers import ProductSerializer, Product

# class OrderItemSerializer(serializers.ModelSerializer):
#     product_details = ProductSerializer(source='product', read_only=True)

#     class Meta:
#         model = OrderItem
#         fields = ['id', 'product', 'product_details', 'quantity', 'price', 'subtotal']
#         read_only_fields = ['price', 'subtotal']

# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True, read_only=True, source='order_items')
#     customer_details = serializers.SerializerMethodField()

#     class Meta:
#         model = Order
#         fields = ['id', 'customer', 'customer_details', 'items', 'total_price', 'status', 'created_at', 'updated_at']
#         read_only_fields = ['customer', 'total_price', 'created_at', 'updated_at']

#     def get_customer_details(self, obj):
#         return {
#             'id': obj.customer.id,
#             'user': {
#                 'id': obj.customer.user.id,
#                 'username': obj.customer.user.username,
#                 'email': obj.customer.user.email
#             },
#             'shipping_address': obj.customer.shipping_address,
#             'billing_address': obj.customer.billing_address,
#             'phone_number': obj.customer.phone_number
#         }

#     def create(self, validated_data, *args, **kwargs):
#         products_data = validated_data.pop('items')
#         customer_profile = self.context['request'].user.customerprofile
#         order = Order.objects.create(customer=customer_profile, **validated_data)

#         for product_data in products_data:
#             product = Product.objects.get(id=product_data['id'])
#             quantity = product_data['quantity']
#             OrderItem.objects.create(
#                 order=order,
#                 product=product,
#                 quantity=quantity,
#                 price=product.price
#             )

#         order.save()
#         return order

# from rest_framework import serializers
# from .models import Order, OrderItem
# from products.serializers import ProductSerializer, Product
# # from customers.serializers import CustomerProfileSerializer

# class OrderItemSerializer(serializers.ModelSerializer):
#     product_details = ProductSerializer(source='product', read_only=True) # Include product details using ProductSerializer

#     class Meta:
#         model = OrderItem
#         # Fields to include in the serialization 
#         fields = ['id', 'product', 'product_details', 'quantity', 'price', 'subtotal']
#         # Fields that should be read-only
#         read_only_fields = ['price', 'subtotal']

# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True, read_only=True) # Use the reverse relation name
#     product_details = ProductSerializer(source='products', many=True, read_only=True)
#     customer_details = serializers.SerializerMethodField() # Method field to include customer details
#     class Meta:
#         model = Order
#         fields = ['id', 'customer', 'customer_details', 'product_details', 'items', 'total_price', 'status', 'created_at', 'updated_at']
#         read_only_fields = ['customer', 'total_price', 'created_at', 'updated_at']

#     def get_customer_details(self, obj):
#         return {
#             'id': obj.customer.id,
#             'user': {
#                 'id': obj.customer.user.id,
#                 'username': obj.customer.user.username,
#                 'email': obj.customer.user.email
#             },
#             'shipping_address': obj.customer.shipping_address,
#             'billing_address': obj.customer.billing_address,
#             'phone_number': obj.customer.phone_number
#         }

#     def create(self, validated_data):
#         # Remove products from validated_data
#         products_data = validated_data.pop('products',)
#         # quantities_data = validated_data.pop('quantities',) # Assuming quantities are send from frontend
#         customer_profile = self.context['request'].user.customerprofile
#         order = Order.objects.create(customer=customer_profile, **validated_data)

#         for product_data in products_data:
#             product = Product.objects.get(id=product_data['product_id']) # Assuming product_id is sent from frontend
#             quantity = product_data['quantity']
#             OrderItem.objects.create(
#                 order=order,
#                 product=product,
#                 quantity=quantity,
#                 price=product.price # Or get the price from product_data if sent from frontend
#             )
#             order.products.add(product)

#         order.save()    # Recalculate total price (which now uses OrderItems)
#         return order


        # Get the customer profile from the request
        # try:
        #     customer_profile = self.context['request'].user.customerprofile
        # except AttributeError:
        #     raise serializers.ValidationError("Customer profile not found for this user")
        
        # # Create the order
        # order = Order.objects.create(customer=customer_profile, **validated_data)
        
        # # Add products to the order
        # for product_id in products_data:
        #     product = Product.objects.get(id=product_id)
        #     order.products.add(product)
        
        # # Recalculate total price
        # order.save()
        
        # return order
    # def create(self, validated_data):
    #     # Remove 'customer' from validated_data to avoid conflict
    #     validated_data.pop('customer', None)

    #     try:
    #         customer_profile = self.context['request'].user.customerprofile
    #     except AttributeError:
    #         raise serializers.ValidationError("Customer profile not found for this user")

    #     order = Order.objects.create(customer=customer_profile, **validated_data)
    #     return order

    # def create(self, validated_data):
    #     customer = self.context['request'].user.customerprofile
    #     order = Order.objects.create(customer=customer, **validated_data)
    #     return order
        # def get_customer_details(self, obj):    # Method to add customer details to the serialization
        #     return {
        #         'id': obj.customer.id,
        #         'username': obj.customer.username,
        #         'email': obj.customer.email
        #     }

        # # Custom create method to handle nested items data
        # def create(self, validated_data):
        #     # Extract products data
        #     products_data = validated_data.pop('products', [])
            
        #     # Create the order with customer
        #     customer = self.context['request'].user
        #     order = Order.objects.create(customer=customer, **validated_data)
            
        #     # Add products to the order
        #     for product_id in products_data:
        #         product = Product.objects.get(id=product_id)
        #         order.products.add(product)
            
        #     # Recalculate total price
        #     order.save()
            
        #     return order
    
            # # Extract nested items data
            # items_data = validated_data.pop('items', [])

            # Create the order with customer
            # customer = self.context['request'].user # Get the current user
            # order = Order.objects.create(customer=customer, **validated_data)   # Create the order
            # return order
            # Process each item from the requested data
            # items_data = self.context['request'].data.get('items', [])
            # for item_data in items_data:
            #     product = Product.objects.get(id=items_data['product'])
            #     OrderItem.objects.create(
            #         order = order,
            #         product = product,
            #         quantity = item_data['quantity']
            #     )     
            # # Save the order to trigger total price calculation     
            # order.save() 

            # return order
# class OrderSerializer(serializers.ModelSerializer):
#     # Include related data for read operations
#     product_details = ProductSerializer(source='product', read_only=True)
#     customer_details = CustomerProfileSerializer(source='customer', read_only=True)
#     class Meta:
#         model = Order
#         fields = ['id', 'customer', 'product', 'quantity', 'total_price', 'status', 'created_at', 'updated_at']

#         # These fields should be automatically handled by the system
#         read_only_fields = ['total_price', 'created_at', 'updated_at']