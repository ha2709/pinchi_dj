from rest_framework import permissions

class IsDepartmentStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and hasattr(request.user, 'department'):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.category.department == request.user.department
