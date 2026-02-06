from django.shortcuts import render
from .models import Tasks 
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request, 'taskmanagement_app/home.html')
def tasks(request):
    tasks = Tasks.objects.all()
    context = {'tasks' : tasks}
    return render(request,'taskmanagement_app/tasks.html', context)
def task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    context = {'task' : task}
    return render(request, 'taskmanagement_app/task.html', context)
def addtask(request): 
    pass
def updatetask(request, task_id):
    pass
def deletetask(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('taskmanagement_app:tasks'))
