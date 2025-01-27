from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet, NotaServicioViewSet

router = DefaultRouter()
router.register(r'pedidos_almacen', PedidoViewSet)
router.register(r'notas', NotaServicioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]