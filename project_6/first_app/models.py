from django.db import models

# Create your models here.
class Students(models.Model):
    roll=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    address=models.TextField()
    fathers_name=models.TextField(default='Rahim')

    def __str__(self):
        return f"roll : {self.roll} , name : {self.name}"