from django.db import models
from django.conf import settings

class Room(models.Model):

    STATUS_CHOICES = [
        ("WAITING","Waiting"),
        ("ACTIVE","Active"),
        ("FINISHED","Finished"),
    ]

    room_code=models.CharField(max_length=6,unique=True)

    player1 = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="rooms_created",)
    player2 = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="rooms_joined",blank=True,null=True,)

    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="WAITING",)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_code