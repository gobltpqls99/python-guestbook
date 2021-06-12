





from django.urls import path
from . import views




app_name ='account'
urlpatterns = [
    path('', views.main, name="main"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.join, name='signup'),
]