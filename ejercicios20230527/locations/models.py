from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return "{}".format(self.name)

class City(models.Model):
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        # return "{} - {}".format(self.department, self.name)
        return "{}".format(self.name)

class District(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return "{}".format(self.name)
