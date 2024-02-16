from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import register

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'homeafterlogin.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'homepage.html')
    else:
        return render(request,'homepage.html')

def logout(request):
    auth.logout(request)
    return render (request,'homepage.html')
def register1(request):
    # if request.method == "POST":
        return render (request,'register.html')
def register2(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        if register.objects.filter(email=email).exists():
            messages.info(request, 'OOPS! email already taken')
            return render(request, 'homepage.html')
        else:
            user = register.objects.create(username=username, password=password,name=name,email=email)
            user.save()
            messages.info(request, 'Account created successfully!!')
            return render(request, 'homepage.html')
@login_required(login_url='home1')
def homepage2(request):
    return render(request, 'homeafterlogin.html')