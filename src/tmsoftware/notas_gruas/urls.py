from django.urls import path
from .views import CrearNotaAPIView

urlpatterns = [
    path('api/notas_gruas/', CrearNotaAPIView.as_view(), name='notas_gruas_api'),
]