from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('settings/', views.settings, name='settings'),
]
