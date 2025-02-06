## pedir a utils calcular horas que haga sus calculos

## pedir al api que envie la nota al backend a su base de datos

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from utils.api_client import enviar_datos  # Importamos la función para enviar los datos
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Formulario(BoxLayout):
    cliente = StringProperty("")
    fecha = StringProperty("")
    hora_salida = StringProperty("")
    hora_llegada = StringProperty("")
    hora_termino = StringProperty("")
    hora_regreso = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Aquí también puedes agregar inicializaciones si es necesario.

    def enviar_datos(self):
        """Cuando el usuario presiona el botón, mandamos los datos a la base de datos."""
        
        # Asegúrate de que todos los datos sean capturados correctamente
        datos = {
            "cliente": self.cliente,
            "fecha": self.fecha,
            "hora_salida": self.hora_salida,
            "hora_llegada": self.hora_llegada,
            "hora_termino": self.hora_termino,
            "hora_regreso": self.hora_regreso,
        }
        
        # Llamamos a la función que envía los datos al servidor
        enviar_datos(datos)