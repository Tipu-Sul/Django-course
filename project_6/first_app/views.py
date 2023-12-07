from django.shortcuts import render,redirect
from .import models

# Create your views here.
def home(request):
    students=models.Students.objects.all()
    return render(request, 'first_app/home.html' ,{'data':students})

def delete_students(request,roll):
    std=models.Students.objects.all().get(pk=roll).delete()
    return redirect("home")


