from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Nota
from .serializers import NotaSerializer
from django.http import JsonResponse
from creadorPDF.utils import generar_pdf, enviar_whatsapp

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer