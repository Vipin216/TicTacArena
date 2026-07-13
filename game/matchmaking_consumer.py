import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import MatchmakingQueue


class MatchmakingConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope["user"]

        if not user.is_authenticated:
            self.close()
            return
        
        self.group_name = f"matchmaking_{user.id}"

        async_to_sync(
            self.channel_layer.group_add
        )(
            self.group_name,
            self.channel_name,
        )

        self.accept()

        print(f"{user.username} joined {self.group_name}")

    
    def disconnect(self, close_code):

        MatchmakingQueue.objects.filter(
            player=self.scope["user"]
        ).delete()
        async_to_sync(
            self.channel_layer.group_discard
        )(
            self.group_name,
            self.channel_name,
        )


        print(f"Left{self.group_name}")
        
    
    def match_found(self,event):
        self.send(
            text_data=json.dumps(
                {
                    "type":"match_found",
                    "room_code":event["room_code"],
                }
            )
        )