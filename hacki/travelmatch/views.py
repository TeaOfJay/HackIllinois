from django.shortcuts import render
from django.http import HttpResponse

appname = 'travelmatch/'

def index(request):
    return render(request, appname + 'index.html')

def login(request):
    return render(request, appname + 'login.html')

def where(request):
    return render(request, appname + 'where.html')

def who(request):
    return render(request, appname + 'who.html')

def myfunction(request):
    return render(request, appname + 'who.html')

# Create your views here.





