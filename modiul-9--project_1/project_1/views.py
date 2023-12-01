from django.http import HttpResponse

def home(request):
    return HttpResponse("this is a homepage")


def contract(request):
    return HttpResponse("this is a contract request!")

    