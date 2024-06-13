from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView,
                          HabitDestroyAPIView, PublicHabitListAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit-list'),
    path('public/', PublicHabitListAPIView.as_view(), name='public-habit-list'),
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-view'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-edit'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
]
