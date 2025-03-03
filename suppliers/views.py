from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from models import Supplier
from serializers import SupplierSerializer
from permissions import IsSupplierRole

# Create your views here.
class SupplierView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsSupplierRole]