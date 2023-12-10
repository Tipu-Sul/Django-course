from django.shortcuts import render
from taskmodel.models import Task
from categorymodel.models import TaskCategory

# def home(request):
#     data=Task.objects.all()
#     return render(request, 'home.html',{'data':data})

def home(request):
    data=TaskCategory.objects.all()
    return render(request, 'home.html',{'data':data})