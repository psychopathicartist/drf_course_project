from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='testuser@myapp.ru', password='123')
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            author=self.user,
            place='тестовое место',
            time='12:00:00',
            action='тестовое действие',
            is_pleasant=False,
            periodicity=2,
            reward='тестовая награда',
            time_to_complete=120,
            is_public=True
        )

    def test_habit_retrieve(self):
        """
        Тестирование просмотра привычки
        """

        url = reverse('habits:habit-view', args=[self.habit.pk])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('place'), self.habit.place)

    def test_habit_create(self):
        """
        Тестирование создания привычки
        """

        url = reverse('habits:habit-create')
        data = {'place': 'тестовое место2', 'time': '12:00:00', 'action': 'тестовое действие2', 'is_pleasant': False,
                'time_to_complete': 120}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        """
        Тестирование редактирования привычки
        """

        url = reverse('habits:habit-edit', args=[self.habit.pk])
        data = {'time_to_complete': '60'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('time_to_complete'), '60')

    def test_habit_delete(self):
        """
        Тестирование удаления привычки
        """

        url = reverse('habits:habit-delete', args=[self.habit.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        """
        Тестирование выведения списка привычек
        """

        url = reverse('habits:habit-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_public_habit_list(self):
        """
        Тестирование выведения списка публичных привычек
        """

        url = reverse('habits:public-habit-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)
