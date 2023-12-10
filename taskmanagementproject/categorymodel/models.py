from django.db import models
from taskmodel.models import Task

# Create your models here.
class TaskCategory(models.Model):
    categoryName = models.CharField(max_length=100)
    title=models.ManyToManyField(Task)

    def __str__(self):
        return self.categoryName