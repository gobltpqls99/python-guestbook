






from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

def main(request):
    return render(request, "main/index.html")


def login(request):
    if request.method == "POST":
        account = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = account, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("main:index")
        else :
            return render(request, "main/error.html")
    else :
        return render(request, "account/login.html")
        

def logout(request):
    if request.user.is_authenticated :
        auth_logout(request)
    return redirect("main:index")


def join(request):
    if request.method=="GET" :
        return render(request, "account/signup.html")
    elif request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            new_user = User.objects.create_user(username=request.POST['username'], password = request.POST['password'])
            auth.login(request, new_user)
            new_user.save()
            return redirect('main:index')
    return render(request, "account/signup.html")


