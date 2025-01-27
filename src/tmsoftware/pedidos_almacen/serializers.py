from rest_framework import serializers
from .models import Pedido, NotaServicio

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class NotaServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaServicio
        fields = '__all__'