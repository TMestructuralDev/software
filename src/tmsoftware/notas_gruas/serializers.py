from rest_framework import serializers
from .models import Nota

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = [
            'id', 'cliente', 'telefono', 'fecha', 'empresa', 'ubicacion',
            'equipo', 'operador', 'ayudante', 'trabajo_realizado', 
            'hora_salida', 'hora_llegada', 'hora_termino', 'hora_regreso', 
            'costo_hora', 'total_horas', 'total_sin_iva', 'total_con_iva', 
            'pdf_file'
        ]