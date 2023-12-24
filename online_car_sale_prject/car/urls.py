from django.urls import path
from. import views

urlpatterns = [
    path('details/<int:id>/',views.CarDetailView.as_view(),name='detail'),
    path('signup/',views.create_user,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/<int:id>/',views.EditProfileView.as_view(),name='edit_profile'),
    path('login/',views.login_user_view.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('buy/<int:id>/',views.copy_car,name='buy'),
]

