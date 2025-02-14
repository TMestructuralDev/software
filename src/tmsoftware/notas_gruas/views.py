from rest_framework import viewsets
from .models import Nota
from .serializers import NotaSerializer
from rest_framework.permissions import AllowAny

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    permission_classes = [AllowAny]