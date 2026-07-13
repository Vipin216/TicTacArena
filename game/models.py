from django.db import models
from django.conf import settings


class Room(models.Model):

    STATUS_CHOICES = [
        ("WAITING", "Waiting"),
        ("ACTIVE", "Active"),
        ("FINISHED", "Finished"),
    ]

    room_code = models.CharField(
        max_length=6,
        unique=True,
    )

    player1 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rooms_created",
    )

    player2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rooms_joined",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="WAITING",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    # Current game state
    board = models.JSONField(
        default=list,
    )

    current_turn = models.CharField(
        max_length=1,
        default="X",
    )

    winner = models.CharField(
        max_length=1,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.room_code


class Match(models.Model):

    room = models.OneToOneField(
        Room,
        on_delete=models.CASCADE,
        related_name="match",
    )

    player1 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="matches_as_player1",
    )

    player2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="matches_as_player2",
    )

    winner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="won_matches",
    )

    is_draw = models.BooleanField(
        default=False,
    )

    played_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        if self.is_draw:
            return f"{self.player1} vs {self.player2} (Draw)"

        return f"{self.player1} vs {self.player2} - Winner: {self.winner}"
    



class MatchmakingQueue(models.Model):
    player=models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    joined_at=models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.player.username