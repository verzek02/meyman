from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
<<<<<<< HEAD
        return request.user.is_staff
=======
        return request.user.is_staff
>>>>>>> Eldiyar
