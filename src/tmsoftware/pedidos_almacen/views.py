from rest_framework import viewsets
from .models import Ingeniero, Material, Pedido, PedidoMaterial
from .serializers import IngenieroSerializer, MaterialSerializer, PedidoSerializer, PedidoMaterialSerializer

class IngenieroViewSet(viewsets.ModelViewSet):
    queryset = Ingeniero.objects.all()
    serializer_class = IngenieroSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoMaterialViewSet(viewsets.ModelViewSet):
    queryset = PedidoMaterial.objects.all()
    serializer_class = PedidoMaterialSerializer
