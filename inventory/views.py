from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from inventory.models import InventoryLog
from inventory.serializers import InventoryLogSerializer
from suppliers.permissions import IsSupplier

# Create your views here.

class InventoryLogView(viewsets.ModelViewSet):
    serializer_class = InventoryLogSerializer
    permission_classes = [IsSupplier]

    def get_queryset(self):
        return InventoryLog.objects.filter(product__supplier=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = serializer.validated_data['product']
        if product.supplier != request.user:
            return Response({"error": "You do not own this product"}, status=status.HTTP_403_FORBIDDEN)
        
        # Update product stock based on inventory action
        if serializer.validated_data['action'] == 'increase':
            product.stock += serializer.validated_data['quantity']
        elif serializer.validated_data['action'] == 'decrease':
            product.stock -= serializer.validated_data['quantity']
        product.save()
