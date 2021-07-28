from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated and (obj.owner == request.user or request.user.is_staff)
        )
