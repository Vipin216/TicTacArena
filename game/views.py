from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room
from .forms import JoinRoomForm
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




@login_required
def join_room(request):

    if request.method=="POST":

        form=JoinRoomForm(request.POST)
        if form.is_valid():
            room_code = form.cleaned_data["room_code"].upper()

            try:
                room=Room.objects.get(room_code=room_code)
            
            except Room.DoesNotExist:

                form.add_error("room_code","Room does not exist.")
            
            else:
                if room.player1 == request.user:
                    form.add_error("room_code","You cannot join your own room.")
                
                elif room.player2 is not None:
                    form.add_error("room_code","Room is already full.")
                
                else:
                    room.player2 = request.user
                    room.status = "ACTIVE"
                    room.save()

                    return redirect("game_room",room.room_code)
                
    else:
        form = JoinRoomForm()

    return render(request,"game/join_room.html",{"form":form})




@login_required
def game_room(request,room_code):
    room=get_object_or_404(Room,room_code=room_code)
    return render(request,"game/game_room.html",{"room":room})