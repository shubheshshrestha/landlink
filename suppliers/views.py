from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from .models import Supplier
from .serializers import SupplierSerializer
from .permissions import IsSupplier

# Create your views here.
class SupplierView(ModelViewSet):
    # queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsSupplier]

    def get_queryset(self):
        return Supplier.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        if not serializer.validated_data.get('phone_number'):
            raise serializer.ValidationError({'phone_number': 'This field is required.'})
        serializer.save(user=self.request.user)