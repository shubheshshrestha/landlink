from rest_framework import permissions

class IsSupplier(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and (hasattr(request.user, 'supplier') or request.user.role == 'Supplier'))
    
class IsSupplierOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_authenticated and request.user.role == 'Supplier'