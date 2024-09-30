from django.urls import path

from .views import *
from .views import TaskDetailView

app_name = 'tasks'

urlpatterns = [
    path('', index, name='tasks_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]