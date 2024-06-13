from django.contrib.auth.models import AbstractUser
from django.db import models

from habits.models import NULLABLE


class User(AbstractUser):
    """
    Модель пользователя, где в качестве основного поля выступает электронная почта
    """

    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    name = models.CharField(max_length=100, verbose_name='имя', **NULLABLE)
    town = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    chat_id = models.CharField(max_length=100, verbose_name='id чата в Telegram', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
