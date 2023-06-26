from django.contrib import admin
from django.urls import path, include
from locations import views

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from locations.views import DepartmentViewSet, CityViewSet, DistrictViewSet

router = DefaultRouter()
router.register('Department', DepartmentViewSet, basename='Departamento')
router.register('City', CityViewSet, basename='Ciudad')
router.register('District', DistrictViewSet, basename='Barrio')

app_name = "locations"
urlpatterns = [
    path('locations', views.all), 
    path('locations/departamentos', views.departamentos, name = 'departamentos'),
    path('locations/departamentos/<str:name_department>', views.ciudades),
    path('locations/departamentos/<str:name_department>/<str:name_city>', views.barrios),
    path('api_locations/', include(router.urls)),
]
