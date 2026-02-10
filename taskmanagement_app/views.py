from django.shortcuts import render,get_object_or_404
from .models import Tasks 
from django.http import HttpResponseRedirect, JsonResponse
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
    if request.method == "POST":
        task = request.POST.get('task')
        deadline = request.POST.get('due-date')
        description = request.POST.get('description')
        error = False
        if not task and not deadline:
            error = True
            context = {'error' : error}
            return render(request,'taskmanagement_app/addtask.html', context)
        Tasks.objects.create(title = task, deadline = deadline, description = description)
        return HttpResponseRedirect(reverse('taskmanagement_app:tasks'))
    return render(request,'taskmanagement_app/addtask.html')
def updatetask(request, task_id):
    task = Tasks.objects.get(id=task_id)
    
    if request.method == "POST":
        new_task = request.POST.get('task')
        new_desc = request.POST.get('description')
        new_due_date=request.POST.get('due-date')

        error = False

        if new_task:
            task.title = new_task
            task.description = new_desc
            task.deadline = new_due_date
            task.save()
            return HttpResponseRedirect(reverse('taskmanagement_app:tasks'))
        else:
            error = True
            context = {'task' : task, 'error' : error}
            return render(request,'taskmanagement_app/updatetask.html', context)
    context = {'task' : task}
    return render(request, 'taskmanagement_app/updatetask.html', context)

def deletetask(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('taskmanagement_app:tasks'))
def tasks_events_json(request):
    tasks = Tasks.objects.all()

    events = []
    for task in tasks:
        events.append({
            'id': task.id,
            'title': task.title,
            'deadline': task.deadline.isoformat() if task.deadline else None,
            'url' : reverse('taskmanagement_app:updatetask', args=[task.id]),
            'extendedProps' : {
                'description': task.description
            } 
        })
    return JsonResponse(events, safe=False)
def calendar_view(request):
    return render(request, 'taskmanagement_app/calendar.html')