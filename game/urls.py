from django.urls import path
from . import views


urlpatterns = [
    path("create-room/",views.create_room,name="create_room"),
    path("room/<str:room_code>/",views.waiting_room,name="waiting_room"),
    path("join-room/",views.join_room,name="join_room"),
    path("game/<str:room_code>/",views.game_room,name="game_room"),
    path("history/",views.match_history,name="match_history"),
    path("find-match/",views.find_match,name="find-match"),
    path("matchmaking/",views.matchmaking,name="matchmaking"),
    path("leaderboard/",views.leaderboard,name="leaderboard"),
    path("profile/<str:username>/",views.player_profile,name="player_profile",),
]