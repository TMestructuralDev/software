import os
from dotenv import load_dotenv
from twilio.rest import Client

# Cargar variables de entorno desde .env
load_dotenv()

class PDF_envio():
    
    def enviar_pdf(pdf_url, telefono):
        
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        # Enviar PDF por WhatsApp
        message = client.messages.create(
            from_="whatsapp:+14155238886",  # Número de Twilio WhatsApp
            body="Aquí tienes tu archivo PDF",
            to=f"whatsapp:+52{telefono}",  # Número de destino
            media_url=pdf_url
        )

        print(f"Mensaje enviado: {message.sid}")
        print(f"Estado del mensaje: {message.status}") 