from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from .models import Supplier
from .serializers import SupplierSerializer
from .permissions import IsSupplierRole

# Create your views here.
class SupplierView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsSupplierRole]

    def get_queryset(self):
        return Supplier.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)