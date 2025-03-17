from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderView

router = DefaultRouter()
router.register(r'orders', OrderView, basename='orders')

urlpatterns = [
    path('', include(router.urls))
]