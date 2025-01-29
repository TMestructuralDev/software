from rest_framework import serializers
from .models import Ingeniero, Material, Pedido, PedidoMaterial

class IngenieroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingeniero
        fields = ['id', 'ingeniero']  # Se mantiene igual

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'nombre', 'cantidad']

class PedidoMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()  # Se mantiene igual

    class Meta:
        model = PedidoMaterial
        fields = ['id', 'material', 'cantidad', 'fecha']  # 🔹 Se agregó 'cantidad'

class PedidoSerializer(serializers.ModelSerializer):
    ingeniero = serializers.StringRelatedField()  # 🔹 Ahora muestra el nombre del ingeniero
    materiales = PedidoMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'ingeniero', 'fecha_solicitud', 'materiales']