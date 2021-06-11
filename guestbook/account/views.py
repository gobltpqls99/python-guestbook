






from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

def main(request):
    return render(request, "main/index.html")


def login(request):
    if request.method == "POST":
        account = request.POST['account']
        password = request.POST['password']
        user = authenticate(username = account, password=password)
        if user is not None:
            auth_login(request, user)
        else :
            return render(request, "main/error.html")
        return redirect("main:index")
    else :
        return render(request, "account/login.html")
        

def logout(request):
    if request.user.is_authenticated :
        auth_logout(request)
    return redirect("main:index")


def join(request):
    if request.method=="GET" :
        return render(request, "account/join.html")
    elif request.method == "POST":
        new_user = User.objects.create_user(username=request.POST['username'], password = request.POST['password'])
        new_user.save()
        return render(request, "account/join.html")


