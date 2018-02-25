from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
import configparser
import time
import datetime
from datetime import timedelta, date
from .models import User_Data
import jwt
import os

dir = os.path.dirname(__file__)

appname = 'travelmatch/'
Config = configparser.ConfigParser()
Config.read(r'C:\config.ini')

def index(request):
    if 'TOKEN' not in request.COOKIES:
        return HttpResponseRedirect("/travelmatch/unauthorized")
    return render(request, appname + 'index.html')

def login(request):
    return render(request, appname + 'login.html')

def where(request):
    if 'TOKEN' not in request.COOKIES:
        return HttpResponseRedirect("/travelmatch/unauthorized")
    return render(request, appname + 'where.html')
def wplans(request):
    return render(request, appname + 'wplans.html')

def who(request):
    if 'TOKEN' not in request.COOKIES:
        return HttpResponseRedirect("/travelmatch/unauthorized")
    webtoken = jwt.decode(request.COOKIES['TOKEN'], 'secret', algorithms=['HS256'])
    print(webtoken)
    query = User_Data.objects.filter(user_id=webtoken.userid)
    if (len(query) == 1):
        print(query)
    return render(request, appname + 'who.html')

def unauthorized(request):
    return render(request, appname + 'unauthorized.json')

def callback(request):
    # Exchange code for access token
    params = {
        'client_id': Config['Keys']['ClientId'],
        'redirect_uri': 'https://743a17e3.ngrok.io/travelmatch/_callback',
        'client_secret': Config['Keys']['ClientSecret'],
        'code': request.GET.get('code','')
    }
    r = requests.get('https://graph.facebook.com/v2.12/oauth/access_token', params=params)
    if 'access_token' in r.json():
        # Verify access token
        accessToken = r.json()['access_token']
        params = {
            'input_token': r.json()['access_token'],
            'access_token': Config['Keys']['AccessToken']
        }
        r = requests.get('https://graph.facebook.com/debug_token', params=params)

        facebookId = r.json()['data']['user_id']
        userQuery = User_Data.objects.filter(user_id=r.json()['data']['user_id'])
        response = HttpResponseRedirect("/travelmatch/who")
        
        if (len(userQuery) == 0):
            # Create entry for new user (if not already existant)
            user = User_Data()
            user.user_id = r.json()['data']['user_id']
            # Get user name
            headers = {
                'Authorization': 'Bearer ' + accessToken
            }
            r = requests.get('https://graph.facebook.com/v2.12/' + user.user_id, headers=headers)
            user.name = r.json()['name']
            # Get profile image
            params = {
                'redirect': 'false'
            }
            r = requests.get('https://graph.facebook.com/v2.12/' + user.user_id + '/picture', headers=headers, params=params)
            user.image_url = r.json()['data']['url']
            # Get likes
            headers = {
                'Authorization': 'Bearer ' + accessToken
            }
            r = requests.get('https://graph.facebook.com/v2.12/' + user.user_id + '/likes', headers=headers)
            user.likes = r.json()['data']
            user.save()
        token = jwt.encode({'userid': facebookId}, 'secret')
        response.set_cookie('TOKEN', token[2:])
        return response
    return HttpResponseRedirect("/travelmatch/unauthorized")

def loginRedirect(request):
    # Redirect to OAuth provider
    return HttpResponseRedirect("https://www.facebook.com/v2.12/dialog/oauth?client_id=586126661725961&redirect_uri=https://743a17e3.ngrok.io/travelmatch/_callback&state=/&scope=user_likes,email")
