from rest_framework.serializers import ValidationError


class RelatedOrRewardValidator:
    """
    Валидатор для проверки того, что поле вознаграждения и
    поле связанной привычки одновременно не заполнены
    """

    def __init__(self, field_first, field_second):
        self.field_first = field_first
        self.field_second = field_second

    def __call__(self, habit):
        if habit.get('related_habit') and habit.get('reward'):
            raise ValidationError('Нельзя заполнить одновременно и поле вознаграждения, и поле связанной привычки!')


class TimeToCompleteValidator:
    """
    Валидатор для проверки того, что время выполнения привычки всегда меньше 120 секунд
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        if habit.get('time_to_complete') > 120:
            raise ValidationError('Время выполнения привычки должно быть не больше 120 секунд!')


class IsPleasantAndRelatedValidator:
    """
    Валидатор для проверки того, что при указании связанной привычки,
    туда могут попасть только привычки с признаком приятной
    """

    def __init__(self, field_first, field_second):
        self.field_first = field_first
        self.field_second = field_second

    def __call__(self, habit):
        related_habit = habit.get('related_habit')
        if related_habit:
            if not related_habit.is_pleasant:
                raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной '
                                      'привычки!')


class IsPleasantValidator:
    """
    Валидатор для проверки того, что у приятной привычки не указано
    вознаграждение или связанная привычка
    """

    def __init__(self, field_first, field_second, field_third):
        self.field_first = field_first
        self.field_second = field_second
        self.field_third = field_third

    def __call__(self, habit):
        if habit.get('is_pleasant'):
            if habit.get('related_habit') or habit.get('reward'):
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки!')


class PeriodicityValidator:
    """
    Валидатор для проверки того, что периодичность выполнения привычки
    нельзя установить реже 1 раза в неделю
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        if habit.get('periodicity'):
            if habit.get('periodicity') > 7 or habit.get('periodicity') < 1:
                raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней!')
