from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.userlogin,name='login'),
    path('logout/', views.userlogout,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('pass_change/', views.pass_change,name='pass_change'),
    path('pass_change2/', views.pass_change2,name='pass_change2'),
]
