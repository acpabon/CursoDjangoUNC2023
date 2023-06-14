from django.contrib import admin
from django.urls import path, include
from myapp import views

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from myapp.views import MascotaViewSet, EspecieViewSet

router = DefaultRouter()
router.register('mascotas', MascotaViewSet, basename='mascotas')
router.register('especies', EspecieViewSet, basename='especies')


app_name = "app"
urlpatterns = [
    path('', views.index),
    path('index2', views.index_2), 

    path('lists_persons', views.lists_persons, name='lists_persons'), 
    path('lists_persons_json', views.lists_persons_json), 
    path('person/<int:id>', views.detail_person, name='detail_person'), 
    path('person/<int:id>/pets', views.list_pets_persons, name='list_pets_persons'), 
    
    path('lists_pets', views.lists_pets, name='lists_pets'),
    path('pet/<str:name>', views.detail_pet, name = 'detail_pet'), 
    path('pet/<str:name>/observation', views.detail_pet_observation, name='observations_pet'), 
    
    path('specie/<int:id>', views.detail_specie), 

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
