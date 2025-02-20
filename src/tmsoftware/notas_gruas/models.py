from django.db import models
from .pdf_generador import generar_pdf  # Importamos la función para generar PDF
from .pdf_envio import PDF_envio

###   ###   ###   ###   ###   ###   ###   ###

class Nota(models.Model):
    cliente = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
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
    costo_hora = models.IntegerField()
    total_horas = models.FloatField()
    total_sin_iva = models.FloatField()
    total_con_iva = models.FloatField()
    pdf_file = models.FileField(upload_to="notas_pdfs/", blank=True, null=True)  # Campo para almacenar el PDF
    pdf_url = models.URLField(blank=True, null=True) 

    
    def __str__(self):
        return f"Nota de {self.cliente} - {self.fecha}"
    
    def save(self, *args, **kwargs):
        """Llama a la función de generación de PDF al guardar el modelo"""
        
        if not self.pk:  # Solo guarda la primera vez
            super().save(*args, **kwargs)  

        pdf_path, pdf_url = generar_pdf(self)  # Genera el PDF
        self.pdf_file.name = pdf_path  # Guarda la ruta del PDF en el modelo
        self.pdf_url = f"http://127.0.0.1:8000{pdf_url}"

        super().save(update_fields=["pdf_file", "pdf_url"])  # Guarda nuevamente solo el campo PDF
        
        # Envía el PDF por WhatsApp al cliente
        # PDF_envio.enviar_pdf(self.pdf_url, self.telefono)
        
        print (self.pdf_url)