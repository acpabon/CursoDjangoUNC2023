from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()

    def __str__(self) -> str:
        return "{} {}".format(self.name, self.last_name)

class Mascot(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return "{}".format(self.name)
