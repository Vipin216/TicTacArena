from django.contrib import admin
from .models import Room,Match,MatchmakingQueue


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "room_code",
        "player1",
        "player2",
        "status",
        "created_at",
    )


admin.site.register(Match)
admin.site.register(MatchmakingQueue)