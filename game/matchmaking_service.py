from django.db import transaction
from .models import MatchmakingQueue,Room
import random
import string
from .utils import generate_room_code
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@transaction.atomic
def process_matchmaking(user):
    queue = MatchmakingQueue.objects.select_for_update().order_by("joined_at")

    waiting = queue.exclude(player=user).first()

    if waiting is None:
        MatchmakingQueue.objects.get_or_create(
            player=user
        )

        return None

    room = Room.objects.create(
        room_code = generate_room_code(),
        player1 = waiting.player,
        player2=user,
        status="ACTIVE",
        board=[
            ["","",""],
            ["","",""],
            ["","",""],
        ]
    )

    channel_layer = get_channel_layer()

    async_to_sync(
        channel_layer.group_send
    )(
        f"matchmaking_{waiting.player.id}",
        {
            "type":"match_found",
            "room_code":room.room_code,
        },
    )

    waiting.delete()

    MatchmakingQueue.objects.filter(player=user).delete()

    return room




