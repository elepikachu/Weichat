from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from chat.models import UserImage

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
        password = request.POST['password1']
        User.objects.create_user(username=username, password=password)
        UserImage.objects.create(username=username, img="images/default.jpg")
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


@login_required(login_url="/login")
def upload_view(request):
    if request.method == 'GET':
        img = UserImage.objects.filter(username=request.user)
        if len(img) == 0:
            img = ''
        else:
            img = img[0].img
        dic = {'usr': request.user, 'img': img}
        return render(request, 'upload.html', dic)
    if request.method == 'POST':
        name = request.user
        imgnew = request.FILES.get('img')
        img = UserImage.objects.filter(username=request.user)
        if len(img) == 0:
            UserImage.objects.create(username=name, img=imgnew)
        else:
            img[0].img = imgnew
            img[0].save()


        return HttpResponseRedirect('/')