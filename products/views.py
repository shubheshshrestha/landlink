from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Product
from .serializers import ProductSerializer
from suppliers.permissions import IsSupplier
# from rest_framework.pagination import PageNumberPagination

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSupplier]
    # pagination_class = PageNumberPagination
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['name', 'description']
    # ordering_fields = ['price', 'stock']

    def get_queryset(self):
        return Product.objects.filter(supplier=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(supplier=self.request.user)
        