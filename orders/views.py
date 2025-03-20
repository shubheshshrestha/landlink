from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from suppliers.permissions import IsSupplierOrReadOnly
from customers.permissions import IsCustomer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from customers.models import CustomerProfile

class SupplierOrderView(viewsets.ReadOnlyModelViewSet): # Viewsets for suppliers to view orders containing their products
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsSupplierOrReadOnly]

    def get_queryset(self): # Return orders that include products from the current supplier
        if self.request.user.role == 'Supplier':
            return Order.objects.filter(order_items__product__supplier=self.request.user).distinct()
        return Order.objects.none()
    
class CustomerOrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsCustomer]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Order.objects.none()
        return Order.objects.filter(customer=self.request.user.customerprofile)
    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customerprofile)

# class CustomerOrderView(viewsets.ModelViewSet): # Viewsets for customers to manage their own orders
#     serializer_class = OrderSerializer
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsCustomer]

#     # Return orders belonging to the current customer
#     def get_queryset(self):
#         if not self.request.user.is_authenticated:
#             return Order.objects.none()
#         # Customers can only see their own orders 
#         return Order.objects.filter(customer=self.request.user)
    
#     # Automatically set the current user as the customer when creating an order
#     def perform_create(self, serializer):
#         customer = CustomerProfile.objects.get(user=self.request.user)
#         serializer.save(customer=customer)
        # This increases security as user ID is not needed.
        # serializer.save(customer=self.request.user)

        # items_data = serializer.validated_data.get('items', [])
        # for item_data in items_data:
        #     OrderItem.objects.create(
        #         order=order,
        #         product=item_data['product'],
        #         quantity=item_data['quantity']
        #     )
        
        # Recalculate total price after adding items
        # order.save()
# class OrderView(viewsets.ModelViewSet):
#     serializer_class = OrderSerializer
#     permission_classes = [IsSupplier]

#     def get_queryset(self):
#         return Order.objects.filter(product__supplier=self.request.user) # product__supplier: This syntax tells Django to follow the relationship from Order → Product → User, and filter orders where the supplier of the product matches the specified user (self.request.user).
    
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data) 
