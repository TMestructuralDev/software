from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngenieroViewSet, MaterialViewSet, PedidoViewSet, PedidoMaterialViewSet

router = DefaultRouter()
router.register(r'ingenieros', IngenieroViewSet)
router.register(r'materiales', MaterialViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'pedidos-materiales', PedidoMaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]