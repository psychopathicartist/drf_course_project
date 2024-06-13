import requests
from django.conf import settings


def send_telegram_message(chat_id, message):
    """
    Отправляет сообщение пользователю в Telegram
    """
    print('Сообщение отправлено')
    params = {
        'text': message,
        'chat_id': chat_id
    }
    requests.get(f'{settings.TELEGRAM_URL}{settings.BOT_TOKEN}/sendMessage', params=params)
