from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from habits.models import Habit
from habits.pagination import HabitListPagination
from habits.permissions import IsAuthor
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания привычки
    """

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.author = self.request.user
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    """
    Контроллер для выведения списка привычек
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitListPagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            queryset = Habit.objects.filter(author=user)
        else:
            queryset = Habit.objects.all()
        return queryset


class PublicHabitListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода списка публичных привычек
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitListPagination


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для просмотра привычки
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAdminUser | IsAuthor]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер для изменения привычки
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAdminUser | IsAuthor]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер для удаления привычки
    """

    queryset = Habit.objects.all()
    permission_classes = [IsAdminUser | IsAuthor]
