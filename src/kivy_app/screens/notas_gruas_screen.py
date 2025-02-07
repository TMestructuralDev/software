from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from widgets.date_picker import DatePicker  
from widgets.time_picker import TimePicker
from widgets.formulario_gruas import Formulario
from kivy.properties import StringProperty 

class NotaGruasScreen(MDScreen):
    selected_date = StringProperty("")
    hora_salida = StringProperty("")
    hora_llegada = StringProperty("")
    hora_termino = StringProperty("")
    hora_regreso = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date_picker = DatePicker()
        self.time_picker = TimePicker()
        self.formulario = Formulario()

    def show_date_picker(self, field):
        """Llama al DatePicker y pasa el campo de texto que lo activó."""
        self.date_picker.show_date_picker(field)
        
    def show_time_picker(self, field):
        """Llama al DatePicker y pasa el campo de texto que lo activó."""
        self.time_picker.show_time_picker(field)
        
    def enviar_datos(self):
        """Recopila todos los datos desde el formulario y los envía al backend."""
        self.formulario.enviar_datos()  # Llamamos a la función enviar_datos() de Formulario

    