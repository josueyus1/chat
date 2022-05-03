from django.shortcuts import render

from chat.models import Room
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def login(request):
    return render(request, 'login.html', {
       
    })


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username,password)
    user = authenticate(request,username=username, password=password)
    print (user)
    if user is not None:
        #login(request,user)
       # print(request,user)
        return redirect("/chat/")
    else:
        return redirect("/chat/login")


def index_view(request):
    return render(request, 'index.html', {
        'rooms': Room.objects.all(),
    })


def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'room.html', {
        'room': chat_room,
    })
