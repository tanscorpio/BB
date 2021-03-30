from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home.html'),
    path('signin', views.signin , name='signin.html'),
    path('signup', views.signup , name='signup.html'),
]