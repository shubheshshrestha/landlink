from django.shortcuts import render
from rest_framework import serializers, permissions
from rest_framework.viewsets import ModelViewSet
from .models import Supplier
from .serializers import SupplierSerializer
from .permissions import IsSupplier
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

# Create your views here.
class SupplierView(ModelViewSet):
    # queryset = Supplier.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    serializer_class = SupplierSerializer
    permission_classes = [IsSupplier]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Supplier.objects.none()
        return Supplier.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)