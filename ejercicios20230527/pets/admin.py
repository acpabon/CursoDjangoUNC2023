from django.contrib import admin
from pets.models import Person, Mascot, Specie, Observation

# Register your models here.
admin.site.register(Person)
admin.site.register(Mascot)
admin.site.register(Specie)
admin.site.register(Observation)