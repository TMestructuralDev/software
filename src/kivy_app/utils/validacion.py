import re
from kivy.uix.boxlayout import BoxLayout
from .api_client import ApiClient

class ValidacionFormulario(BoxLayout):
    def enviar_datos(self, datos):
        print("Intentando enviar datos...") 

        mensaje_error = self.validar_datos(datos)

        if mensaje_error:
            print("Error en la validación:", mensaje_error)
            return mensaje_error 
        
        print("Enviando datos al backend...")
        ApiClient.enviar_datos_cliente(datos)
        return None 

    def validar_datos(self, datos):
        """Valida que los datos sean correctos. Retorna un mensaje de error o None si todo es válido."""
        #print("Validando datos:", datos)

        # Validar que los campos obligatorios no estén vacíos
        campos_obligatorios = [
            "cliente", "telefono", "fecha", "empresa", "ubicacion", 
            "equipo", "operador", "trabajo_realizado", "hora_salida", "hora_llegada", "hora_termino", "hora_regreso"
            ]
        for campo in campos_obligatorios:
            if not datos[campo]:
                return f"El campo '{campo}' es obligatorio."

        # Validar que el teléfono tenga 10 dígitos numéricos
        if not re.fullmatch(r"\d{10}", datos["telefono"]):
            return "El teléfono debe contener 10 dígitos numéricos."

        # Validar que la fecha tenga el formato correcto (YYYY-MM-DD)
        if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", datos["fecha"]):
            return "La fecha debe estar en formato DD/MM/YYYY."

        # Validar que las horas tengan el formato correcto (HH:MM)
        for campo_hora in ["hora_salida", "hora_llegada", "hora_termino", "hora_regreso"]:
            if not re.fullmatch(r"\d{2}:\d{2}", datos[campo_hora]):
                return f"La hora en '{campo_hora}' debe estar en formato HH:MM."

        print("Validación exitosa.") 
        return None  # Si todo está bien, no hay error