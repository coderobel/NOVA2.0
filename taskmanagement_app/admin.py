from django.contrib import admin
from .models import Tasks
from NOVA2.routers import MultiDBModelAdmin
# Register your models here.
class TaskAdmin(MultiDBModelAdmin):
    using = 'tasks_db'
    
admin.site.register(Tasks, TaskAdmin)
