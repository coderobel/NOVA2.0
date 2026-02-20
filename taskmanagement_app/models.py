from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=200)
    date_assigned = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    description = models.TextField(max_length=200)
    owner_id = models.IntegerField()
    class Meta:
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
    