from rest_framework import serializers
from .models import Ingeniero, Material, Pedido, PedidoMaterial

class IngenieroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingeniero
        fields = ['id', 'ingeniero']  # Asegúrate de incluir todos los campos que necesites

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'nombre', 'cantidad']

class PedidoMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    ingeniero = IngenieroSerializer()

    class Meta:
        model = PedidoMaterial
        fields = ['id', 'pedido', 'material', 'ingeniero', 'fecha']

class PedidoSerializer(serializers.ModelSerializer):
    ingeniero = IngenieroSerializer()
    materiales = PedidoMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'ingeniero', 'fecha_solicitud', 'materiales']