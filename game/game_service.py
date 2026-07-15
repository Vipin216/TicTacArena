from asgiref.sync import async_to_sync
from .models import Room,Match
import math
from .game_logic import (
    is_cell_empty,
    make_move,
    check_winner,
    is_draw,
)


def save_match(room):

    if Match.objects.filter(room=room).exists():
        return

    if room.winner == "X":

        winner = room.player1

    elif room.winner == "O":

        winner = room.player2

    else:

        winner = None

    Match.objects.create(

        room=room,

        player1=room.player1,

        player2=room.player2,

        winner=winner,

        is_draw=(room.winner == "D"),
    )



def update_player_stats(room):

    if room.winner == "X":

        room.player1.wins += 1
        room.player2.losses += 1

    elif room.winner == "O":

        room.player2.wins += 1
        room.player1.losses += 1

    elif room.winner == "D":

        room.player1.draws += 1
        room.player2.draws += 1

    room.player1.save()
    room.player2.save()




def process_move(consumer, data):

    room = Room.objects.get(room_code=consumer.room_code)

    if room.winner:
        return

    user = consumer.scope["user"]

    if user == room.player1:
        symbol = "X"

    elif user == room.player2:
        symbol = "O"

    else:
        return

    if room.current_turn != symbol:
        return

    board = room.board

    row = int(data["row"])
    col = int(data["col"])

    if not is_cell_empty(board, row, col):
        return

    board = make_move(board, row, col, symbol)

    winner = check_winner(board)

    if winner:
        room.winner = winner

    elif is_draw(board):
        room.winner = "D"

    room.board = board

    room.current_turn = "O" if symbol == "X" else "X"

    room.save()

    if room.winner:
        save_match(room)
        update_player_stats(room)

        if room.winner=="X":
            calculate_elo(room.player1,room.player2,"player1",)
        
        elif room.winner=="O":
            calculate_elo(room.player1,room.player2,"player2",)
        
        else:
            calculate_elo(room.player1,room.player2,"draw",)


    async_to_sync(
        consumer.channel_layer.group_send
    )(
        consumer.room_group_name,
        {
            "type": "move_event",
            "row": row,
            "col": col,
            "symbol": symbol,
            "next_turn": room.current_turn,
            "winner": room.winner,
        }
    )





def calculate_elo(player1,player2,result,k=32):
    expected1 = 1/(1+math.pow(10,(player2.elo - player1.elo)/400))
    expected2 = 1/(1+math.pow(10,(player1.elo - player2.elo)/400))
    if result == "player1":
        score1=1
        score2 = 0
    
    elif result == "player2":
        score1=0
        score2=1

    else:
        score1=0.5
        score2=0.5
    
    player1.elo = round(player1.elo + k*(score1-expected1))
    player2.elo = round(player2.elo + k*(score2-expected2))

    player1.save()
    player2.save()