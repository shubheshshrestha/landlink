from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from delivery.models import Delivery, DeliveryPersonnel
from delivery.serializers import DeliveryPersonnelSerializer, DeliverySerializer
from delivery.permissions import IsDelivery
# Create your views here.

class DeliveryPersonnelView(viewsets.ModelViewSet):
    serializer_class = DeliveryPersonnelSerializer
    permission_classes = [IsDelivery]

    def get_queryset(self):
        return DeliveryPersonnel.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DeliveryView(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer
    permission_classes = [IsDelivery]

    def get_queryset(self):
        return Delivery.objects.filter(delivery_personnel__user=self.request.user)
    
    def perform_create(self, serializer):
        try:
            delivery_personnel = DeliveryPersonnel.objects.get(user=self.request.user)
        except DeliveryPersonnel.DoesNotExist:
            return Response({"error": "No delivery personnel found for this user"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(delivery_personnel=delivery_personnel)
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     # Assign the delivery personnel based on the authenticated user
    #     delivery_personnel = DeliveryPersonnel.objects.get(user=request.user)
    #     serializer.save(delivery_personnel=delivery_personnel)

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)