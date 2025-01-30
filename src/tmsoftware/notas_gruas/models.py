from django.db import models

###   ###   ###   ###   ###   ###   ###   ###

class Nota(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cliente = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    equipo = models.CharField(max_length=50)
    operador = models.CharField(max_length=50)
    ayudante = models.CharField(max_length=50)
    trabajo_realizado = models.TextField()
    hora_salida = models.TimeField()
    hora_llegada = models.TimeField()
    hora_termino = models.TimeField()
    hora_regreso = models.TimeField()
    horas_trabajo = models.FloatField()
    costo_hora = models.IntegerField()
    costo_maniobra = models.FloatField()
    costo_maniobra_iva = models.FloatField()
    
    def __str__(self):
        return f"Nota de {self.cliente} - {self.fecha}"
