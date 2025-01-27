from django.shortcuts import render
from rest_framework import viewsets
from .models import Pedido, NotaServicio
from .serializers import PedidoSerializer, NotaServicioSerializer

# Create your views here.


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class NotaServicioViewSet(viewsets.ModelViewSet):
    queryset = NotaServicio.objects.all()
    serializer_class = NotaServicioSerializer