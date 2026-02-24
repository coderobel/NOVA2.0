from django.shortcuts import render
from .models import Topic,Entry
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    topics = Topic.objects.using('logs_db').filter(owner_id = request.user.id)
    context = {'topics' : topics}
    return render(request, 'learning_logs/home.html', context)
@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    if topic.owner_id != request.user.id:
        raise Http404
    else:
        entries = topic.entry_set.order_by('-date_assigned')
        context = {'topic' : topic, 'entries' : entries}
        return render(request, 'learning_logs/topic.html', context)
@login_required
def newtopic(request):
    if request.method != 'POST':
        form = TopicForm()
    else: 
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.owner_id = request.user.id
            topic.save(using='logs_db')
            return HttpResponseRedirect(reverse('learning_logs:home'))
    context = {'form' : form}
    return render(request, 'learning_logs/newtopic.html', context)
@login_required
def newentry(request, topic_id): 
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'form' : form, 'topic' : topic}
    return render(request,'learning_logs/newentry.html', context)
@login_required
def deletetopic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic.delete()
    return HttpResponseRedirect(reverse('learning_logs:home'))
@login_required
def updatetopic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else: 
        form = TopicForm(data=request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'form' : form, 'topic' : topic}
    return render(request, 'learning_logs/updatetopic.html', context)
@login_required
def deleteentry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    entry.delete()
    return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
@login_required
def updateentry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    context = {'form' : form, 'entry' : entry, 'topic' : topic}
    return render(request, 'learning_logs/updateentry.html', context)