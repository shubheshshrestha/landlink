from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierView

router = DefaultRouter()
router.register(r'suppliers', SupplierView, basename='suppliers')

urlpatterns = [
    path('', include(router.urls))
]
