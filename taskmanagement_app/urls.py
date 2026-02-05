from django.urls import path
from . import views

app_name = 'taskmanagement_app'
urlpatterns = [
    path('', views.home, name='home'),
]