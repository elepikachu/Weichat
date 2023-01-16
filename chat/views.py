from django.shortcuts import render

VERSION = 'WeiChat 1.0.0'


def chat_view(request):
    dic = {'ver': VERSION}
    return render(request, 'chat/chat.html', dic)


def room_view(request, room_name):
    dic = {'ver': VERSION, 'room_name': room_name}
    return render(request, 'chat/room.html', dic)