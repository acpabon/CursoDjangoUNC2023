from django.contrib import admin
from django.urls import path, include
from pets import views

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from pets.views import MascotaViewSet, EspecieViewSet, ObservacionViewSet

router = DefaultRouter()
router.register('mascotas', MascotaViewSet, basename='mascotas')
# router.register('especies', EspecieViewSet, basename='especies')
router.register('observacion', ObservacionViewSet, basename='observacion')

app_name = "pets"
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
