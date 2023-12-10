from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=120)
    taskDecision = models.TextField()
    isCompleted = models.BooleanField(default=False)
    TaskAsaignDate=models.DateField()

    def __str__(self):
        return self.taskTitle