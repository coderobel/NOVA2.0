from django.shortcuts import render
from .models import Topic,Entry
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm
# Create your views here.
def home(request):
    return render(request, 'learning_logs/home.html')
def topics(request):
    topics = Topic.objects.all()
    context = {'topics' : topics}
    return render(request, 'learning_logs/topics.html', context)
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
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form' : form}
    return render(request, 'learning_logs/newtopic.html', context)
def deletetopic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic.delete()
    return HttpResponseRedirect(reverse('learning_logs:topics'))
def deleteentry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    entry.delete()
    return HttpResponseRedirect(reverse('learning_logs:topics'))