from django.shortcuts import render,redirect
from .import forms
from .import models

# Create your views here.
def task(request):
    if request.method =='POST':
        post=forms.AddTask(request.POST)
        if post.is_valid():
            post.save()
            return redirect('task')
    else:
        post=forms.AddTask()
    return render(request,'task.html',{'data':post})


def edit_task(request,id):
    edit_task=models.Task.objects.get(pk=id)
    post=forms.AddTask(instance=edit_task)
    if request.method =='POST':
        post=forms.AddTask(request.POST,instance=edit_task)
        if post.is_valid():
            post.save()
            return redirect('home')
 
    return render(request,'task.html',{'data':post})

def delete_task(request,id):
    delete_task=models.Task.objects.get(pk=id)
    delete_task.delete()
    return redirect('home')


