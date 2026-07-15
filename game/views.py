from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room
from .models import Match,MatchmakingQueue
from .forms import JoinRoomForm
from .utils import generate_room_code
from django.db.models import Q
from .matchmaking_service import process_matchmaking
from users.models import User

@login_required
def create_room(request):
    if request.method != "POST":
        return redirect("lobby")

    room = Room.objects.create(room_code=generate_room_code(),player1=request.user,
        board=[
            ["","",""],
            ["","",""],
            ["","",""]
        ],
    )

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

                    return redirect("waiting_room", room.room_code)
                
    else:
        form = JoinRoomForm()

    return render(request,"game/join_room.html",{"form":form})




@login_required
def game_room(request,room_code):
    room=get_object_or_404(Room,room_code=room_code)
    return render(request,"game/game_room.html",{"room":room})





@login_required
def match_history(request):
    matches = Match.objects.filter(
        Q(player1=request.user)|Q(player2=request.user)).order_by("-played_at")
    
    return render(request,"game/match_history.html",{"matches":matches,},)






@login_required
def find_match(request):

    room = process_matchmaking(request.user)
    if room:
        return redirect("game_room",room_code=room.room_code,)
    
    return redirect("matchmaking")





@login_required
def matchmaking(request):

    MatchmakingQueue.objects.get_or_create(
        player=request.user
    )

    return render(request,"game/matchmaking.html")






def leaderboard(request):
    print("Leaderboard view called")
    players = User.objects.order_by("-elo","-wins")
    print(players)
    return render(request,"game/leaderboard.html",{"players":players,},)





@login_required
def player_profile(request,username):
    player=get_object_or_404(User,username=username)
    matches = Match.objects.filter(Q(player1=player)|Q(player2=player)).order_by("-played_at")[:10]
    return render(request,"game/player_profile.html",{"player":player,"matches":matches,},)