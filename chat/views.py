from django.shortcuts import render
from django.contrib.auth.decorators import login_required

VERSION = 'WeiChat 1.0.0'


@login_required(login_url="/login")
def chat_view(request):
    dic = {'ver': VERSION}
    return render(request, 'chat/chat.html', dic)


@login_required(login_url="/login")
def room_view(request, room_name):
    dic = {'ver': VERSION, 'room_name': room_name, 'user':request.user}
    return render(request, 'chat/room.html', dic)
