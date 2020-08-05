from django.contrib import admin
from django.urls import path
from mypage import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('about', views.about, name = 'about' ),
    path('reply',  views.reply, name = 'reply'),
]