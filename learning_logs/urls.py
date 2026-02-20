from django.urls import path
from . import views
app_name='learning_logs'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('newtopic/', views.newtopic, name='newtopic'),
    path('deletetopic/<int:topic_id>', views.deletetopic, name='deletetopic'),
    path('newentry/<int:topic_id>', views.newentry, name='newentry'),
    path('deleteentry/<int:entry_id>', views.deleteentry, name='deleteentry'),
]