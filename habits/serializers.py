from rest_framework import serializers

from habits.models import Habit
from habits.validators import TimeToCompleteValidator, RelatedOrRewardValidator, IsPleasantValidator, \
    IsPleasantAndRelatedValidator, PeriodicityValidator


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели привычки с валидацией
    """

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedOrRewardValidator(field_first='related_habit', field_second='reward'),
            TimeToCompleteValidator(field='time_to_complete'),
            IsPleasantAndRelatedValidator(field_first='is_pleasant', field_second='related_habit'),
            IsPleasantValidator(field_first='is_pleasant', field_second='related_habit', field_third='reward'),
            PeriodicityValidator(field='periodicity')
        ]
