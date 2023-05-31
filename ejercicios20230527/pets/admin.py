from django.contrib import admin
from pets.models import Person
from pets.models import Mascot

# Register your models here.
admin.site.register(Person)
admin.site.register(Mascot)