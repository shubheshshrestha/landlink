from rest_framework import permissions

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Customer'
    

# # Recommendation:
# If the IsCustomer permission is only used within the customers app, it's fine to keep it there. 
# However, if multiple apps need to use this permission (e.g., orders, notifications), 
# consider moving it to the accounts app to centralize role-based permissions.