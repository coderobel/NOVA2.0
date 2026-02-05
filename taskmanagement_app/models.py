from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=200)
    deadline = models.DateField()
    description = models.TextField(max_length=200)
    class Meta:
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title