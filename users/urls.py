from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('intro/', views.intro, name='intro'),
    path('lesson1/', views.lesson1, name='lesson1'),
    path('lesson2/', views.lesson2, name='lesson2'),
    path('lesson3/', views.lesson3, name='lesson3'),
    path('lesson4/', views.lesson4, name='lesson4'),
    path('lesson5/', views.lesson5, name='lesson5'),
    path('lesson6/', views.lesson6, name='lesson6'),
    path('lesson7/', views.lesson7, name='lesson7'),
    path('lesson8/', views.lesson8, name='lesson8'),
    path('lesson9/', views.lesson9, name='lesson9'),
    path('lesson10/', views.lesson10, name='lesson10'),
    path('lesson11/', views.lesson11, name='lesson11'),
    path('lesson12/', views.lesson12, name='lesson12'),
    path('lesson13/', views.lesson13, name='lesson13'),
    path('preview/', views.preview, name='preview'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]
