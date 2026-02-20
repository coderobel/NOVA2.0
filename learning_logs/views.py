from django.shortcuts import render
from .models import Topic,Entry
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm
# Create your views here.
def home(request):
    topics = Topic.objects.all()
    context = {'topics' : topics}
    return render(request, 'learning_logs/home.html', context)
def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_assigned')
    context = {'topic' : topic, 'entries' : entries}
    return render(request, 'learning_logs/topic.html', context)
def newtopic(request):
    if request.method != 'POST':
        form = TopicForm()
    else: 
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:home'))
    context = {'form' : form}
    return render(request, 'learning_logs/newtopic.html', context)
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
def deletetopic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic.delete()
    return HttpResponseRedirect(reverse('learning_logs:home'))
def updatetopic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else: 
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'form' : form, 'topic' : topic}
    return render(request, 'learning_logs/updatetopic.html', context)
def deleteentry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    entry.delete()
    return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
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