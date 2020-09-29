from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read only
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user

