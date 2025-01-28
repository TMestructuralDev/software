from django.urls import path
from .views import CrearNotaAPIView

urlpatterns = [
    path('api/crear/', CrearNotaAPIView.as_view(), name='crear_nota_api'),
]