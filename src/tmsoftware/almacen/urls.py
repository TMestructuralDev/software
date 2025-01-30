from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet

# Crear un router por defecto
router = DefaultRouter()
router.register(r'almacen', ArticuloViewSet, basename='almacen')

urlpatterns = [
    # Incluir las URLs generadas automáticamente por el router
    path('api/', include(router.urls)),
]