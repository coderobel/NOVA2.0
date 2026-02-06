from django.urls import path
from . import views

app_name = 'taskmanagement_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('task/<int:task_id>', views.task, name='task'),
    path('addtask/', views.addtask, name='addtask'),
    path('updatetask/<int:task_id>', views.updatetask, name= 'updatetask'),
    path('deletetask/<int:task_id>', views.deletetask, name='deletetask'),
]