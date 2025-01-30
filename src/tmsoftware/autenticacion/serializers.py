from rest_framework import serializers
from .models import Ingeniero

class IngenieroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingeniero
        fields = ['id', 'ingeniero', 'nombre']  