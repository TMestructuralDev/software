from rest_framework import serializers
from .models import Nota

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = [
            'id', 'fecha', 'cliente', 'telefono', 'empresa', 'ubicacion',
            'equipo', 'operador', 'ayudante', 'trabajo_realizado', 
            'hora_salida', 'hora_llegada', 'hora_termino', 'hora_regreso', 
            'costo_hora', 'horas_trabajo', 'costo_maniobra', 'costo_maniobra_iva'
        ]