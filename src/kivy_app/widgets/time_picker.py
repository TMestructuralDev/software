from kivymd.uix.pickers import MDTimePicker
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

class TimePicker(MDBoxLayout):
    # Propiedades que se actualizarán en el archivo KV
    hora_salida = StringProperty("")
    hora_llegada = StringProperty("")
    hora_termino = StringProperty("")
    hora_regreso = StringProperty("")
    caller = None  # Campo seleccionado para actualizar

    def show_time_picker(self, caller):
        """Abre el selector de hora y guarda el campo que debe actualizar."""
        self.caller = caller  # Guardamos quién llamó al selector
        time_picker = MDTimePicker()
        time_picker.bind(on_save=self.on_time_selected)  # Vinculamos la función
        time_picker.open()

    def on_time_selected(self, instance, value):
        """Guarda la hora seleccionada y la muestra en el campo de texto que la llamó."""
        time_str = value.strftime("%H:%M")  # Asegura que el formato sea HH:MM
        if self.caller:
            self.caller.text = time_str  # Actualiza el campo de texto del caller