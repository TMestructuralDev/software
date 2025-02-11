## pedir a utils calcular horas que haga sus calculos

## pedir al api que envie la nota al backend a su base de datos

import re
from kivy.uix.boxlayout import BoxLayout
from .api_client import ApiClient

class ValidacionFormulario(BoxLayout):
    def enviar_datos(self, datos):

        mensaje_error = self.validar_datos(datos)

        if mensaje_error:
            print(f"Error: {mensaje_error}")  # Aquí podrías mostrar un mensaje en la interfaz
        else:
            ApiClient.enviar_datos_cliente(datos)

    def validar_datos(self, datos):
        """Valida que los datos sean correctos. Retorna un mensaje de error o None si todo es válido."""

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
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", datos["fecha"]):
            return "La fecha debe estar en formato YYYY-MM-DD."

        # Validar que las horas tengan el formato correcto (HH:MM)
        for campo_hora in ["hora_salida", "hora_llegada", "hora_termino", "hora_regreso"]:
            if not re.fullmatch(r"\d{2}:\d{2}", datos[campo_hora]):
                return f"La hora en '{campo_hora}' debe estar en formato HH:MM."

        return None  # Si todo está bien, no hay error