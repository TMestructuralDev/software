from django.shortcuts import render
from rest_framework import viewsets
from .models import Ingeniero
from .serializers import IngenieroSerializer


# Create your views here.

class IngenieroViewSet(viewsets.ModelViewSet):
    queryset = Ingeniero.objects.all()
    serializer_class = IngenieroSerializer