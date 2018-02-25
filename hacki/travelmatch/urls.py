from django.urls import path

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login', views.login),
    url(r'^where', views.where),
    url(r'^who', views.who),
    url(r'^_callback', views.callback),
    url(r'^unauthorized', views.unauthorized),
    url(r'^facebook_login', views.loginRedirect, name='loginRedirect')

]