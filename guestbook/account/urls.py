from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views

app_name ='accounts'
urlPattern = [
    path('login', views.login, name='login'),
]