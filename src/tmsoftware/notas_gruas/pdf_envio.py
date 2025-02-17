import pywhatkit
import pyautogui
import time

class PDF_envio():
    
    @staticmethod
    def enviar_pdf(pdf_url, numero_destino):
        try:
            
            mensaje = f"{pdf_url}"
            
            numero_destino = f"+52{numero_destino}"

            # Enviar mensaje de WhatsApp con el link al PDF
            pywhatkit.sendwhatmsg_instantly(numero_destino, mensaje)
            time.sleep(5)
            pyautogui.click() 
            time.sleep(1) 
            pyautogui.press("enter")

            print("Mensaje enviado correctamente!")

            # Esperar unos segundos para evitar bloqueos de WhatsApp Web
            

        except Exception as e:
            print(f"Error al enviar el mensaje: {e}")