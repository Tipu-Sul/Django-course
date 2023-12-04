
from django.urls import path
from .import views
urlpatterns = [
    path('menu_items/',views.index ,name='menu_items'),
    path('home/',views.home,name='home' ),
]