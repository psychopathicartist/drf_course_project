from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """
    Модель привычки
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='создатель',
                               **NULLABLE)
    place = models.CharField(max_length=200, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=300, verbose_name='действие')
    is_pleasant = models.BooleanField(verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.IntegerField(default=1, verbose_name='периодичность', **NULLABLE)
    reward = models.TextField(verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.IntegerField(verbose_name='время на выполнение в секундах')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')
    date_to_send = models.DateField(auto_now_add=True, verbose_name='дата ближайшей отправки сообщения', **NULLABLE)

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
