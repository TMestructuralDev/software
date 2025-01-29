from django.db import models
from django.contrib.auth.models import User

class Ingeniero(models.Model):
    ingeniero = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Material(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} - {self.cantidad}"

class Pedido(models.Model):
    ingeniero = models.ForeignKey(Ingeniero, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.ingeniero.nombre}"
    
    '''def lista_materiales(self):
        """Devuelve una lista de materiales con cantidad para este pedido sin usar variables intermedias."""
        return list(self.materiales.values('material__nombre', 'cantidad'))'''

class PedidoMaterial(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='materiales')
    ingeniero = models.ForeignKey(Ingeniero, on_delete=models.CASCADE)
    fecha = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    

    def __str__(self):
        materiales_str = ", ".join([f"{m.material.nombre}: {m.cantidad}" 
                                    for m in self.pedido.materiales.all()])
        
        return f"Ingeniero: {self.ingeniero.nombre}, Fecha: {self.fecha}, Materiales: {materiales_str}"