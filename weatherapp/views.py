from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
import urllib.request
import requests

#weather app from line 11 to 40-------------------------------------------------------------------
# Create your views here.
# @login_required(login_url='home1')
def weather1(request):
    return render(request, 'weatherappinput.html')

def weather2(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '98c9fe0696484df631f05ef073b66aa4'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)

            # Save data to the database
            # WeatherData.objects.create(city=city, temperature=temperature, humidity=humidity)

            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})

#weather app from line 11 to 40-------------------------------------------------------------------

#calculator app----------------------------------------------------------------
def calculator2(request):
    return render(request,'calculator1.html')
def calculator1(request):
    num1 = int(request.GET.get('number1'))
    num2 = int(request.GET.get('number2'))

    if request.GET.get('add') == "":
        ans = num1 + num2

    elif request.GET.get('subtract') == "":
        ans = num1 - num2

    elif request.GET.get('multiply') == "":
        ans = num1 * num2

    else:
        ans = num1 / num2

    return render(request, 'calculator1.html', {'ans': ans})

#calculator app [line 43 to 63]----------------------------------------------------------------