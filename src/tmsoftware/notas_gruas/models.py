from django.db import models
from datetime import datetime, timedelta
from django.dispatch import receiver
from creadorPDF.utils import generar_pdf, enviar_whatsapp
from django.db.models.signals import post_save

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

    def save(self, *args, **kwargs):
        # Calcular la diferencia de horas
        hora_salida = datetime.combine(datetime.today(), self.hora_salida)
        hora_regreso = datetime.combine(datetime.today(), self.hora_regreso)

        # Si la hora de regreso es antes que la hora de salida (cruce de medianoche)
        if hora_regreso < hora_salida:
            hora_regreso += timedelta(days=1)

        # Calcular la diferencia en horas
        diferencia_horas = (hora_regreso - hora_salida).seconds / 3600.0

        # Asignar el valor de horas_trabajo
        self.horas_trabajo = diferencia_horas

        # Calcular los costos
        costo_total = diferencia_horas * self.costo_hora
        costo_total_iva = costo_total * 1.16  # IVA fijo del 16%

        # Asignar los costos al modelo
        self.costo_maniobra = costo_total
        self.costo_maniobra_iva = costo_total_iva

        super(Nota, self).save(*args, **kwargs)
        
@receiver(post_save, sender=Nota)
def procesar_nota(sender, instance, created, **kwargs):
    if created:
        # Generar PDF
        archivo_pdf = generar_pdf(instance)
        
        # Enviar el PDF por WhatsApp al teléfono de la nota
        enviar_whatsapp(archivo_pdf, instance.telefono)