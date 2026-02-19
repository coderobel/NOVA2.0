from django.shortcuts import render
from .models import Topic,Entry
# Create your views here.
def home(request):
    return render(request, 'learning_logs/home.html')
def topics(request):
    topics = Topic.objects.all()
    context = {'topics' : topics}
    return render(request, 'learning_logs/topics.html', context)
def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries}
    return render(request, 'learning_logs/topic.html', context)
def newtopic(request):
    pass
def deletetopic(request, topic_id):
    pass
def deleteentry(request, entry_id):
    pass