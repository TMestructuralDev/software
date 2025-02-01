from django.db import models
from django.contrib.auth.models import User
from autenticacion.models import Ingeniero
from almacen.models import Articulo

###   ###   ###   ###

class Pedido(models.Model):
    ingeniero = models.ForeignKey(Ingeniero, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    material = models.JSONField(default=list) 

    def __str__(self):
        return (
            f"Pedido #{self.id}\n"  
            f"Ingeniero {self.ingeniero.nombre}\n" 
            f"Fecha #{self.fecha}\n" 
            )
