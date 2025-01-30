from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField( max_length=50)
    color = models.CharField(blank=True, null=True, max_length=50)
    medida = models.CharField(blank=True, null=True, max_length=50)
    categoria = models.CharField(blank=True, null=True, max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        # Mostrar todos los atributos concatenados
        return (
        f"Nombre: {self.nombre}\n"
        f"Color: {self.color}\n"
        f"Medida: {self.medida}\n"
        f"Categoria: {self.categoria}\n"
        f"Descripcion: {self.descripcion}"
    )