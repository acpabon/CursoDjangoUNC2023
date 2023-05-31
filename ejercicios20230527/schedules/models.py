from django.db import models
from datetime import datetime

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    cellphone = models.IntegerField()

    def __str__(self) -> str:
        return "{} {}".format(self.name, self.last_name)

class Schedule(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self) -> str:
        return "{}".format(self.description[0:30] + "...")

