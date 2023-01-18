from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

VERSION = 'WeiChat 1.0.0'


# -------------------------------------------------------------
# 函数名： main_view
# 功能： 网站首页
# -------------------------------------------------------------
def main_view(request):
    dic = {'ver': VERSION, 'user': request.user}
    return render(request, 'main.html', dic)


# -------------------------------------------------------------
# 函数名： help_view
# 功能： 网站首页
# -------------------------------------------------------------
def help_view(request):
    dic = {'ver': VERSION}
    return render(request, 'help.html', dic)


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        code = request.POST['code']
        if password2 != password1:
            return HttpResponse('Entered password not matched')
        if code != 'jng':
            return HttpResponse('Inviting code is not correct')
        User.objects.create_user(username=username, password=password1)
        return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if not user:
            return HttpResponse('USERNAME OR PASSWORD ERROR!')
        else:
            login(request, user)
            return HttpResponseRedirect('/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def choose_view(request):
    return render(request, 'choose.html')