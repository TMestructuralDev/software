from rest_framework import serializers
from .models import Pedido
from almacen.models import Articulo

class PedidoSerializer(serializers.ModelSerializer): 
    # Usamos SerializerMethodField para crear un campo calculado
    materiales = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = ['id', 'ingeniero', 'fecha', 'materiales']  # Cambié a 'materiales'

    def get_materiales(self, obj):
        lista_materiales = []
        for item in obj.material:  # obj.material es el JSONField con la lista de diccionarios
            try:
                material = Articulo.objects.get(id=item["id"])  # Buscar el material en la BD usando su id
                lista_materiales.append({
                    "nombre": material.nombre,  # Agregamos el nombre del material
                    "cantidad": item["cantidad"]  # Agregamos la cantidad
                })
            except Articulo.DoesNotExist:
                continue  # Si el material no existe, lo ignoramos
        return lista_materiales