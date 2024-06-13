from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """
    Кастомное право доступа к своему профилю для пользователя
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user
