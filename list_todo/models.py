from django.db import models
from django.utils import timezone

from settings.models import TimeStampedModel


# Create your models here.


class ListTodo(TimeStampedModel):
    '''TODO_ list'''

    IN_PROGRESS = 'in progress'
    DONE = 'done'
    CANCELLED = 'cancelled'
    DELAYED_START = 'delayed start'
    WAIT_FOR_START = 'wait for start'

    DONE_STATUS = (
        (IN_PROGRESS, 'В работе'),
        (DONE, 'Исполнено'),
        (CANCELLED, 'Отменено'),
        (DELAYED_START, 'Отложить начало'),
        (WAIT_FOR_START, 'Ожидает начала')
    )

    task = models.CharField(max_length=200, null=False, blank=False)
    task_description = models.TextField(default='', null=True, blank=True)
    status = models.CharField(max_length=30, choices=DONE_STATUS, default=WAIT_FOR_START, null=False, blank=False)
    start_time = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'