from rest_framework import permissions

class IsAutherReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #safe_methods : GET
            return True
        return obj.author == request.user 