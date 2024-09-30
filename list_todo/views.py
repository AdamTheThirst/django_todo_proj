from django.shortcuts import render

from .models import ListTodo

# Create your views here.

__all__ = (
    'index',
    'TaskDetailView'
)

def index(request):
    qs = ListTodo.objects.all()
    contest = {'objects_list': qs}
    return render(request, 'index.html', contest)

class TaskDetailView(DetailView):
    qeriset = ListTodo.objects.all()
    template_name = 'task_detail.html'