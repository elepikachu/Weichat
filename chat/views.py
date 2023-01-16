from django.shortcuts import render
from django.contrib.auth.decorators import login_required

VERSION = 'WeiChat 1.0.0'


@login_required
def chat_view(request):
    dic = {'ver': VERSION}
    return render(request, 'chat/chat.html', dic)


@login_required
def room_view(request, room_name):
    dic = {'ver': VERSION, 'room_name': room_name}
    return render(request, 'chat/room.html', dic)