from django.core import serializers
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserImage

VERSION = 'WeiChat 1.0.0'


@login_required(login_url="/login")
def chat_view(request):
    dic = {'ver': VERSION}
    return render(request, 'chat/chat.html', dic)


@login_required(login_url="/login")
def room_view(request, room_name):
    imgdic = serializers.serialize("json", UserImage.objects.all())
    dic = {'ver': VERSION, 'room_name': room_name, 'user': request.user, 'imgdic': imgdic}
    return render(request, 'chat/room.html', dic)
