from django.db import models

# Create your models here.

class Pedido(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    cantidad = models.IntegerField()
    material = models.CharField(max_length=100)

    def __str__(self):
        return f"Pedido de {self.nombre} - {self.material}"

class NotaServicio(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_emision = models.DateTimeField(auto_now_add=True)
    generado_por = models.CharField(max_length=100)

    def __str__(self):
        return f"Nota de servicio por {self.pedido.nombre}"