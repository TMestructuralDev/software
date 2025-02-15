import os
from io import BytesIO
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_pdf(nota):
    """Genera un PDF a partir de una instancia de Nota y lo guarda en el servidor."""
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.drawString(100, 750, f"Cliente: {nota.cliente}")
    pdf.drawString(100, 730, f"Teléfono: {nota.telefono}")
    pdf.drawString(100, 710, f"Fecha: {nota.fecha}")
    pdf.drawString(100, 690, f"Empresa: {nota.empresa}")
    pdf.drawString(100, 670, f"Ubicación: {nota.ubicacion}")
    pdf.drawString(100, 650, f"Equipo: {nota.equipo}")
    pdf.drawString(100, 630, f"Operador: {nota.operador}")
    pdf.drawString(100, 610, f"Ayudante: {nota.ayudante}")
    pdf.drawString(100, 590, f"Trabajo Realizado: {nota.trabajo_realizado[:50]}...")
    pdf.drawString(100, 570, f"Hora de salida: {nota.hora_salida}")
    pdf.drawString(100, 550, f"Hora de llegada: {nota.hora_llegada}")
    pdf.drawString(100, 530, f"Hora de término: {nota.hora_termino}")
    pdf.drawString(100, 510, f"Hora de regreso: {nota.hora_regreso}")
    pdf.drawString(100, 490, f"Costo por hora: ${nota.costo_hora}")
    pdf.drawString(100, 470, f"Total de horas: {nota.total_horas}")
    pdf.drawString(100, 450, f"Total sin IVA: ${nota.total_sin_iva}")
    pdf.drawString(100, 430, f"Total con IVA: ${nota.total_con_iva}")
    pdf.save()

    buffer.seek(0)

    # Definir la carpeta donde se guardarán los PDFs
    pdf_folder = os.path.join(settings.MEDIA_ROOT, "notas_pdfs")
    os.makedirs(pdf_folder, exist_ok=True)

    # Ruta del archivo PDF
    pdf_filename = f"nota_{nota.id}.pdf"
    pdf_path = os.path.join(pdf_folder, pdf_filename)

    # Guardar el PDF en la carpeta de medios
    with open(pdf_path, "wb") as f:
        f.write(buffer.getvalue())

    return os.path.join("notas_pdfs", pdf_filename)  # Devolver la ruta relativa del PDF