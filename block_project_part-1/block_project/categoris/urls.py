from django.urls import path
from .import views

urlpatterns = [
    path('add/', views.add_categoris, name='add_category'),
]