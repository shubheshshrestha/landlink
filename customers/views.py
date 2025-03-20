from django.shortcuts import render
from rest_framework import viewsets, permissions
from customers.models import CustomerProfile
from customers.serializers import CustomerProfileSerializer
from customers.permissions import IsCustomer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# Create your views here.

class CustomerProfileView(viewsets.ModelViewSet):
    serializer_class = CustomerProfileSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsCustomer]

    def get_queryset(self):
        return CustomerProfile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
