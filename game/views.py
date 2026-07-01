from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room
from .utils import generate_room_code


@login_required
def create_room(request):
    if request.method != "POST":
        return redirect("lobby")

    room = Room.objects.create(room_code=generate_room_code(),player1=request.user,)

    return redirect("waiting_room",room.room_code)


@login_required
def waiting_room(request,room_code):
    room=get_object_or_404(Room,room_code=room_code)

    return render(request,"game/waiting_room.html",{"room":room})