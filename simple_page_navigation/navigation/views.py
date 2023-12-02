from django.shortcuts import render

# Create your views here.
# def create(request):
#     return render(request,"I love Django app")

def about(request):
    return render(request, 'navigation/about.html')

def contract(request):
    return render(request, 'navigation/contract.html')