from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from suppliers.permissions import IsSupplier

# Create your views here.

class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsSupplier]

    def get_queryset(self):
        return Order.objects.filter(product__supplier=self.request.user) # product__supplier: This syntax tells Django to follow the relationship from Order → Product → User, and filter orders where the supplier of the product matches the specified user (self.request.user).
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 