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

# Model specie
class Specie(models.Model):
    kinds = [
        ("D", "Domestico"),
        ("W", "Silvestre")
    ]
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=1, choices=kinds, default="D")

    def __str__(self) -> str:
        return "{}-{}".format(self.name, self.get_kind_display())
    
class Observation(models.Model):
    pet = models.ForeignKey(Mascot, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
    file = models.FileField()

    def __str__(self) -> str:
        return "{} - {} - {}".format(self.pet.name, self.description[0:20], self.date)