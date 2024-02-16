from django.conf import settings
from django.urls import path, include
from . import views
from django.conf.urls.static import static



# app_name = 'navbar'
urlpatterns = [
    path('',views.homepage, name = 'home1'),
    path('register1',views.register1, name = 'register1'),
    path('register2',views.register2, name = 'register2'),
    path('login',views.login, name = 'login'),
    path('home2',views.homepage2, name = 'home2'),
    path('logout',views.logout, name = 'logout'),


    ]

