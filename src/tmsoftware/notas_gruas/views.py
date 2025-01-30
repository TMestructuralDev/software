from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Nota
from .serializers import NotaSerializer
from django.http import JsonResponse
from creadorPDF.utils import generar_pdf, enviar_whatsapp

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    def create(self, request, *args, **kwargs):
        # Serializar los datos recibidos
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Guardar la nueva nota
            nueva_nota = serializer.save()

            # Generar el PDF y enviarlo por WhatsApp
            archivo_pdf = generar_pdf(nueva_nota)
            enviar_whatsapp(archivo_pdf, nueva_nota.telefono)

            # Devolver una respuesta exitosa
            return JsonResponse({'message': 'Nota creada con éxito y enviada por WhatsApp'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)