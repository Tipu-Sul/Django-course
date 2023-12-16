from django.urls import path,include
from. import views

urlpatterns = [
    path('',views.set_session, name='home'),
    path('get/',views.get_session, name='cookie'),
    path('del/',views.delete_cookie, name='del-cookie'),
    path('del_ses/',views.delete_session, name='del-session'),
]