from django.urls import path, include
from . import views



# app_name = 'navbar'
urlpatterns = [
    path('send1/',views.sendingmail1, name = 'send1'),
    path('send2/',views.sendingmail2, name = 'send2'),


]
