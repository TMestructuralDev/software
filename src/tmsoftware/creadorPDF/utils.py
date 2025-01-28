# creadorpdf/utils.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from twilio.rest import Client
import os

def generar_pdf(nota):
    archivo_pdf = f"nota_{nota.id}.pdf"
    archivo_ruta = os.path.join("media", "notas", archivo_pdf)

    # Crear el PDF
    c = canvas.Canvas(archivo_ruta, pagesize=letter)

    # Escribir los datos en el PDF
    c.drawString(100, 750, f"Fecha: {nota.fecha}")
    c.drawString(100, 735, f"Cliente: {nota.cliente}")
    c.drawString(100, 720, f"Empresa: {nota.empresa}")
    c.drawString(100, 705, f"Ubicación: {nota.ubicacion}")
    c.drawString(100, 690, f"Equipo: {nota.equipo}")
    c.drawString(100, 675, f"Operador: {nota.operador}")
    c.drawString(100, 660, f"Trabajo Realizado: {nota.trabajo_realizado}")
    c.drawString(100, 645, f"Horas de trabajo: {nota.horas_trabajo}")
    c.drawString(100, 630, f"Costo Maniobra: ${nota.costo_maniobra}")
    c.drawString(100, 615, f"Costo Maniobra con IVA: ${nota.costo_maniobra_iva}")

    c.save()

    return archivo_ruta

def enviar_whatsapp(pdf_file, numero_destino):
    client = Client("TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN") # IMPORTANTE: crear cuenta de twilio y reemplazar estos datos
    
    # Envía el mensaje por WhatsApp con el archivo PDF adjunto
    mensaje = client.messages.create(
        body="Aquí está tu nota de servicio",
        from_='whatsapp:+526694452803',  # Número de Twilio
        to=f'whatsapp:{numero_destino}',  # Número de destino
        media_url=[pdf_file]
    )
    
    return mensaje.sid