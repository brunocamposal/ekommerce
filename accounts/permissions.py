from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_staff & request.user.is_superuser) is False


class IsSalesman(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff & (request.user.is_superuser is False)
