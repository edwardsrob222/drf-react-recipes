from rest_framework import permissions

class IsOwnerORReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return true
        return obj.created_by == request.user
