from django.shortcuts import render
from django.http import HttpResponse

appname = 'travelmatch/'

def index(request):
    return render(request, 'travelmatch/index.html')

#def login(request):
#    return render(request, travelmatch + 'login.html')

# Create your views here.





