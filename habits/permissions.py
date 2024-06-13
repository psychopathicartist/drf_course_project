from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """
    Кастомное право доступа для создателя привычки
    """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
