from django.db import models
import datetime

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Game (models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return str(self.team1)
