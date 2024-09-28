from django.shortcuts import render

from .models import ListTodo

# Create your views here.

def index(request):
    qs = ListTodo.objects.all()
    contest = {'objects_list': qs}
    return render(request, 'list_todo/index.html', contest)