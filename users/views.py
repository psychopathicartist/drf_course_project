from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from users.models import User
from users.permissions import IsUser
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания пользователя с хешированием пароля
    """

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """
    Контроллер для выведения списка пользователей
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для просмотра пользователя
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser | IsUser]


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер для изменения пользователя
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser | IsUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер для удаления пользователя
    """

    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
