from django.contrib import admin
from locations.models import Department
from locations.models import City
from locations.models import District

# Register your models here.
admin.site.register(Department)
admin.site.register(City)
admin.site.register(District)