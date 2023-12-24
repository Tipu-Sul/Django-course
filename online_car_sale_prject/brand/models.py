from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    description = models.TextField()
    slug=models.SlugField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.brand_name