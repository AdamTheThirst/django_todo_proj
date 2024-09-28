from django.contrib import admin

from .models import ListTodo

# Register your models here.

@admin.register(ListTodo)
class CustomListTodoAdmin(admin.ModelAdmin):
    list_display = (
        'task_kind',
        'task',
        'task_description',
        'status',
        'start_time',
    )

    list_filter = (
        'task_kind',
        'task',
        'status',
        'start_time',
    )