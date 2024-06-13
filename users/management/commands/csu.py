from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Кастомная команда, которая запускается из консоли и создает суперюзера
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@myapp.ru",
            is_active=True,
            is_staff=True,
            is_superuser=True
        )

        user.set_password("123456")

        user.save()
