from twilio.rest import Client

class PDF_envio():

    def enviar_pdf_twilio(pdf_url, numero_destino):
        # Credenciales de Twilio
        account_sid = 'tu_account_sid'
        auth_token = 'tu_auth_token'
        client = Client(account_sid, auth_token)

        # Enviar el mensaje con el archivo PDF
        message = client.messages.create(
            body="Aquí está el PDF de la nota que solicitaste",
            from_='whatsapp:+14155238886',  # El número de WhatsApp de Twilio
            to=f'whatsapp:{numero_destino}',  # El número de destino
            media_url=[pdf_url]  # URL pública del PDF que has cargado
        )

        print(f"Mensaje enviado: {message.sid}")