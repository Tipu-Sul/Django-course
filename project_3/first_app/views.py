from django.shortcuts import render
import datetime
# Create your views here.
def view(request):
    d={'author':'rahim', 'age':10 ,'lst':["python",'is','my','favorite','language'],
       'val':' ', 'birthday':datetime.datetime.now(),'courses':[
    {
        'id':1,
        "name": 'c',
        'fee':100
    },
    {
        'id':1,
        "name": 'c++',
        'fee':100
    },
    {
        'id':1,
        "name": 'python',
        'fee':100
    }
    ]}
    # d['can_drive']=d['age']>=20
    return render(request, 'first_app/index.html',d)