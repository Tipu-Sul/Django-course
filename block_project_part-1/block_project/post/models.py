from django.db import models
from categoris.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Category)#single post can be in multipe categories and multiple post can be in in categories
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
   
    def __str__(self):
       return self.title


