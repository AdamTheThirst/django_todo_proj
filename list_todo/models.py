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

    PERSONAL = 'personal'
    WORK = 'work'
    EDUCATION = 'education'
    KIDS = 'kids'
    OTHER = 'other'

    TASK_KINDS = (
        (PERSONAL, 'личное'),
        (WORK, 'работа'),
        (EDUCATION, 'обучеие'),
        (KIDS, 'дети'),
        (OTHER, 'иное'),
    )

    task = models.CharField(max_length=200, null=False, blank=False, verbose_name='Задача')
    task_description = models.TextField(default='', null=True, blank=True, verbose_name='Пояснение')
    task_kind = models.CharField(max_length=20, choices=TASK_KINDS, null=False, blank=False, default='PERSONAL', verbose_name='Тип задачи')
    status = models.CharField(max_length=30, choices=DONE_STATUS, default=WAIT_FOR_START, null=False, blank=False, verbose_name='Статус')
    start_time = models.DateTimeField(null=True, blank=True, default=timezone.now, verbose_name='Время начала')
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='Дэдлайн')

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-start_time']