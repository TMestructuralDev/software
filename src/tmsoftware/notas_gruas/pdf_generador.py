import os
from io import BytesIO
import textwrap
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def generar_pdf(nota):
    """Genera un PDF con personalización: logo, colores y mejor diseño."""
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    # Configurar fuentes y colores
    pdf.setFont("Helvetica-Bold", 14)
    pdf.setFillColorRGB(0, 0, 0)  # Color naranja para títulos

    # Agregar logo (ajusta la ruta de la imagen)
    logo_path = os.path.join(settings.MEDIA_ROOT, "logo_empresa.png")  # Ruta del logo
    if os.path.exists(logo_path):
        pdf.drawImage(logo_path, 450, 720, width=120, height=60, preserveAspectRatio=True)

    # Encabezado
    pdf.drawString(100, 750, "NOTA DE SERVICIO")  # Título
    pdf.setFont("Helvetica", 14)
    pdf.setFillColorRGB(0, 0, 0) 

    # Información de la nota
    y = 700  # Posición inicial en Y
    espacio = 20  # Espacio entre líneas

    datos = [
    ("Cliente", nota.cliente),
    ("Teléfono", nota.telefono),
    ("Fecha", str(nota.fecha)),  
    ("Empresa", nota.empresa),
    ("Ubicación", nota.ubicacion),
    ("Equipo", nota.equipo),
    ("Operador", nota.operador),
    ("Ayudante", nota.ayudante),
    ("", ""),  # Línea en blanco para separación
    ("Trabajo Realizado", nota.trabajo_realizado[:150] + "..."),
    ("", ""),  # Línea en blanco para separación
    ("Hora de salida", str(nota.hora_salida)),  
    ("Hora de llegada", str(nota.hora_llegada)), 
    ("Hora de término", str(nota.hora_termino)),  
    ("Hora de regreso", str(nota.hora_regreso)), 
    ("Costo por hora", f"${nota.costo_hora}"),
    ("Total de horas", str(nota.total_horas)),
    ("", ""),  # Línea en blanco para separación
    ("Total sin IVA", f"${nota.total_sin_iva}"),
    ("Cuenta para pago sin IVA", ""), 
    ("Paulina Guadalupe Manjarrez Tirado", "BBVA"), 
    ("No. Cuenta", "156 992 9903"), 
    ("No. Cuenta CLABE", "012 180 0156 9929 9031"), 
    ("", ""),  # Línea en blanco para separación
    ("Total con IVA", f"${nota.total_con_iva}"),
    ("Cuenta para pago con IVA", ""), 
    ("CIMA Ingenieria Estructural", "BBVA"), 
    ("No. Cuenta", "011 922 8780"), 
    ("No. Cuenta CLABE", "012 744 0011 9228 7806"), 
] 

    for titulo, valor in datos:
        
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(100, y, f"{titulo}:")
        
        if titulo == "Trabajo Realizado":
            pdf.setFont("Helvetica", 12)
            # Envolver el texto con un ancho de 70 caracteres
            wrapped_text = textwrap.wrap(valor, width=50)
            for linea in wrapped_text:
                pdf.drawString(350, y, linea)  # Imprime cada línea de trabajo realizado
                y -= espacio  # Mueve hacia abajo por cada línea del texto envuelto
        else:
            pdf.setFont("Helvetica", 12)
            pdf.drawString(350, y, valor)  # Imprime los demás valores
            y -= espacio  # Mueve hacia abajo por cada línea normal

    # Agregar línea separadora
    pdf.setStrokeColor(colors.black)
    pdf.line(80, y, 500, y)

    pdf.save()
    buffer.seek(0)

    # Guardar el PDF en el servidor
    pdf_folder = os.path.join(settings.MEDIA_ROOT, "notas_pdfs")
    os.makedirs(pdf_folder, exist_ok=True)

    pdf_filename = f"nota_{nota.id}.pdf"
    pdf_path = os.path.join(pdf_folder, pdf_filename)

    with open(pdf_path, "wb") as f:
        f.write(buffer.getvalue())

    pdf_url = f"{settings.MEDIA_URL}notas_pdfs/{pdf_filename}"

    return os.path.join("notas_pdfs", pdf_filename), pdf_url