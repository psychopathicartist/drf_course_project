# Generated by Django 5.0.6 on 2024-06-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='date_to_send',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='дата ближайшей отправки сообщения'),
        ),
    ]
