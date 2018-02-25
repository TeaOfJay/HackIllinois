from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
import configparser

appname = 'travelmatch/'
Config = configparser.ConfigParser()
Config.read("config.ini")

def index(request):
    return render(request, appname + 'index.html')

def login(request):
    return render(request, appname + 'login.html')

def where(request):
    return render(request, appname + 'where.html')

def who(request):
    return render(request, appname + 'who.html')

def unauthorized(request):
    return render(request, appname + 'unauthorized.json')

def callback(request):
    print(request.GET.get('code',''))
    params = {
        'client_id': Config['Keys']['ClientId'],
        'redirect_uri': 'https://b84c3ce6.ngrok.io/travelmatch/_callback',
        'client_secret': Config['Keys']['ClientSecret'],
        'code': request.GET.get('code','')
    }
    r = requests.get('https://graph.facebook.com/v2.12/oauth/access_token', params=params)
    print(r.json())
    if 'access_token' in r.json():
        params={
            'input_token': r.json()['access_token'],
            'access_token': Config['Keys']['AccessToken']
        }
        r = requests.get('https://graph.facebook.com/debug_token', params=params)
        print(r.json())
        return HttpResponseRedirect("/travelmatch/who")
    return HttpResponseRedirect("/travelmatch/unauthorized")

def loginRedirect(request):
    return HttpResponseRedirect("https://www.facebook.com/v2.12/dialog/oauth?client_id=586126661725961&redirect_uri=https://b84c3ce6.ngrok.io/travelmatch/_callback&state=/&scope=user_likes")

# Create your views here.





