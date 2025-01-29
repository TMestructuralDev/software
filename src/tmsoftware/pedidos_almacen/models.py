from django.db import models
from django.contrib.auth.models import User

class Ingeniero(models.Model):
    ingeniero = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingeniero.username  # Asegurar que devuelve el nombre correctamente

class Material(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} - {self.cantidad}"

class Pedido(models.Model):
    ingeniero = models.ForeignKey(Ingeniero, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.ingeniero.ingeniero.username}"

class PedidoMaterial(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='materiales')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)  # Agregar cantidad
    fecha = models.DateTimeField(auto_now_add=True)  # Ahora almacena la fecha correctamente

    def __str__(self):
        return f"Pedido {self.pedido.id} - {self.material.nombre}: {self.cantidad}"