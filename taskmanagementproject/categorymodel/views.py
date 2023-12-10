from django.shortcuts import render,redirect
from .import forms

# Create your views here.
def category(request):
    if request.method =='POST':
        post=forms.AddTaskCategory(request.POST)
        if post.is_valid():
            post.save()
            return redirect('category')
    else:
        post=forms.AddTaskCategory()
    return render(request, 'category.html',{'data':post})