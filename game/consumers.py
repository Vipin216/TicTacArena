import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .game_service import process_move
from .models import Room



class GameConsumer(WebsocketConsumer):

    def connect(self):

        self.room_code = self.scope["url_route"]["kwargs"]["room_code"]

        self.room_group_name = f"room_{self.room_code}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        self.accept()
        room = Room.objects.get(room_code=self.room_code)

        if self.scope["user"] == room.player1:
            your_symbol = "X"
        else:
            your_symbol = "O"
        self.send(
            text_data=json.dumps(
                {
                    "type": "game_state",
                    "board": room.board,
                    "current_turn": room.current_turn,
                    "winner": room.winner,
                    "your_symbol":your_symbol,
                }
        )
    )

        

        print(f"{self.channel_name} joined {self.room_group_name}")

        

        room = Room.objects.get(room_code=self.room_code)

        if room.player2:

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "game_start",
                }
            )



    def disconnect(self, close_code):


        async_to_sync(
            self.channel_layer.group_discard
        )(
            self.room_group_name,
            self.channel_name,
        )
        async_to_sync(
            self.channel_layer.group_send
        )(
            self.room_group_name,
            {
                "type":"player_disconnected",
                "username":self.scope["user"].username,
            }
        )
        print(f"{self.channel_name} left {self.room_group_name}")




    def receive(self, text_data):

        data = json.loads(text_data)

        if data["type"] == "move":
            process_move(self, data)
    


    def chat_message(self, event):

        message = event["message"]

        self.send(
            text_data=json.dumps(
                {
                    "message": message,
                }
            )
        )


    def game_start(self, event):

        self.send(
            text_data=json.dumps(
                {
                    "type": "game_start"
                }
            )
        )


    def move_event(self, event):

        self.send(
            text_data=json.dumps(
                {
                    "type": "move",
                    "row": event["row"],
                    "col": event["col"],
                    "symbol": event["symbol"],
                    "next_turn": event["next_turn"],
                    "winner":event["winner"],
                }
            )
        )

    

    def player_disconnected(self,event):
        self.send(
            text_data=json.dumps(
                {
                    "type":"player_disconnected",
                    "username":event["username"],
                }
            )
        )