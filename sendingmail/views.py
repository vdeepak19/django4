from django.shortcuts import render

# Create your views here.
def sendingmail1(request):
    return render(request,'sendingmail.html')

def sendingmail2(request):
    return "abc"