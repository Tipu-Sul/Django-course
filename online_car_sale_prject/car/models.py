from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    car_image = models.FileField(upload_to='car/media/uploads/',blank=True,null=True)
    car_name = models.CharField(max_length=150)
    car_price = models.CharField(max_length=100,blank=True,null=True)
    car_quantity = models.IntegerField(blank=True, null=True)
    car_brand_name=models.ForeignKey(Brand, on_delete=models.CASCADE)
    def __str__(self):
        return self.car_name
    

class Comment(models.Model):
    car=models.ForeignKey(Car, on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"comments by {self.name}"


class BuyedCar(models.Model):
    car_image = models.FileField(upload_to='car/media/uploads/',blank=True,null=True)
    car_name = models.CharField(max_length=150)
    car_price = models.CharField(max_length=100,blank=True,null=True)
    car_quantity = models.IntegerField(blank=True, null=True)
    car_brand_name=models.ForeignKey(Brand, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    slug=models.SlugField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.car_name
    


