from django.db import models


# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=256)
    complete = models.BooleanField(default=False)
    task_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name