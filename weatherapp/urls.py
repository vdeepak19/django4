from django.conf import settings
from django.urls import path, include
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('w/',views.weather1, name = 'weather1'),
    path('weatherresult/',views.weather2, name = 'weather2'),
    path('calculator1/',views.calculator1,name='calculator1'),
    path('calculator2/',views.calculator2,name='calculator2'),



    ]

