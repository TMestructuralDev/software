from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from widgets.date_picker import DatePicker  
from widgets.time_picker import TimePicker
from utils.validacion import ValidacionFormulario
from kivy.properties import StringProperty 

class NotaGruasScreen(MDScreen):
    
    cliente = StringProperty("")
    telefono = StringProperty("")
    fecha = StringProperty("")
    empresa = StringProperty("")
    ubicacion = StringProperty("")
    equipo = StringProperty("")
    operador = StringProperty("")
    ayudante = StringProperty("")
    trabajo_realizado = StringProperty("")
    hora_salida = StringProperty("")
    hora_llegada = StringProperty("")
    hora_termino = StringProperty("")
    hora_regreso = StringProperty("")
    costo_hora = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date_picker = DatePicker()
        self.time_picker = TimePicker()
        self.validacion_formulario = ValidacionFormulario()

    def show_date_picker(self, field):
        """Llama al DatePicker y pasa el campo de texto que lo activó."""
        self.date_picker.show_date_picker(field)
        
    def show_time_picker(self, field):
        """Llama al DatePicker y pasa el campo de texto que lo activó."""
        self.time_picker.show_time_picker(field)
        
    def enviar_datos(self):
        """Recopila todos los datos desde el formulario y los envía al backend."""
        self.validacion_formulario .enviar_datos() # Llamamos a la función enviar_datos()

    def enviar_datos(self):
        """Recopila todos los datos desde el formulario y los envía al backend."""
        # Recopilamos los datos directamente de los campos del formulario
        datos = {
            "cliente": self.ids.cliente.text.strip(),
            "telefono": self.ids.telefono.text.strip(),
            "fecha": self.ids.fecha.text.strip(),
            "empresa": self.ids.empresa.text.strip(),
            "ubicacion": self.ids.ubicacion.text.strip(),
            "equipo": self.ids.equipo.text.strip(),
            "operador": self.ids.operador.text.strip(),
            "ayudante": self.ids.ayudante.text.strip(),
            "trabajo_realizado": self.ids.trabajo_realizado.text.strip(),
            "hora_salida": self.ids.hora_salida.text.strip(),
            "hora_llegada": self.ids.hora_llegada.text.strip(),
            "hora_termino": self.ids.hora_termino.text.strip(),
            "hora_regreso": self.ids.hora_regreso.text.strip(),
            "costo_hora": self.ids.costo_hora.text.strip(),
        }

        # Llama al método de validación y posterior envío
        self.validacion_formulario.enviar_datos(datos)