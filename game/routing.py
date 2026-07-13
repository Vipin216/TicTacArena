from django.urls import re_path
from .matchmaking_consumer import MatchmakingConsumer

from game import consumers

websocket_urlpatterns=[
    re_path(r"ws/game/(?P<room_code>\w+)/$",consumers.GameConsumer.as_asgi(),),
    re_path(r"ws/matchmaking/$",MatchmakingConsumer.as_asgi(),),
]
