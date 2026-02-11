from django.shortcuts import render,get_object_or_404
from .models import Tasks 
from django.http import HttpResponseRedirect, JsonResponse,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    return render(request, 'taskmanagement_app/home.html')
@login_required
def tasks(request):
    tasks = Tasks.objects.filter(owner=request.user).order_by('deadline')
    context = {'tasks' : tasks}
    return render(request,'taskmanagement_app/tasks.html', context)
@login_required
def task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    if task.owner != request.user:
        raise Http404
    context = {'task' : task}
    return render(request, 'taskmanagement_app/task.html', context)
@login_required
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
        Tasks.objects.create(title = task, deadline = deadline, description = description, owner=request.user)
        return HttpResponseRedirect(reverse('taskmanagement_app:tasks'))
    return render(request,'taskmanagement_app/addtask.html')
@login_required
def updatetask(request, task_id):
    task = Tasks.objects.get(id=task_id)
    if task.owner != request.user:
        raise Http404
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
@login_required
def deletetask(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('taskmanagement_app:tasks'))
@login_required
def tasks_events_json(request):
    tasks = Tasks.objects.all()

    events = []
    for task in tasks:
        events.append({
            'id': task.id,
            'title': task.title,
            'start': task.deadline.isoformat() if task.deadline else None,
            'url' : reverse('taskmanagement_app:task', args=[task.id]),
            'extendedProps' : {
                'description': task.description
            } 
        })
    return JsonResponse(events, safe=False)
@login_required
def calendar_view(request):
    return render(request, 'taskmanagement_app/calendar.html')