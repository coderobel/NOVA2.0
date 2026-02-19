from django.contrib import admin
from .models import Topic,Entry
from NOVA2.routers import MultiDBModelAdmin
# Register your models here.
class TopicAdmin(MultiDBModelAdmin):
    using = 'logs_db'
class EntryAdmin(MultiDBModelAdmin):
    using = 'logs_db'
admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)