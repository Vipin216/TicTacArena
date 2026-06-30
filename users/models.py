from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    wins=models.PositiveIntegerField(default=0)
    losses = models.PositiveBigIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    elo = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.username
    
