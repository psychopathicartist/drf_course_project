from datetime import timedelta
from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message
from django.utils import timezone


@shared_task
def compose_and_send_message_task():
    """
    Рассылает напоминания о выполнении привычки пользователям в Telegram
    """

    habits = Habit.objects.all()

    for habit in habits:
        chat_id = habit.author.chat_id
        if habit.time <= timezone.now().time() and habit.date_to_send == timezone.now().date() and chat_id:
            reward_text = ''
            if habit.reward:
                reward_text = f'Награда за выполнение: {habit.reward}'
            elif habit.related_habit:
                reward_text = f'После выполнения можете {habit.related_habit.action} в {habit.related_habit.place}'
            message = f'Напоминание: Вам нужно {habit.action.lower()} в {habit.place.lower()}. {reward_text.lower()}'
            send_telegram_message(chat_id, message)

            habit.date_to_send = habit.date_to_send + timedelta(days=habit.periodicity)
            habit.save()
