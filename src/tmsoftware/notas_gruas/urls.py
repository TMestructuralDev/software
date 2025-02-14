from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet

# Crear un router por defecto
router = DefaultRouter()
router.register(r'notas_gruas', NotaViewSet, basename='notas_gruas')

urlpatterns = [
    # Incluir las URLs generadas automáticamente por el router
    path('', include(router.urls)),
]