from kivymd.uix.pickers import MDTimePickerInput
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
        self.caller = caller  
        self.time_picker = MDTimePickerInput()
        self.time_picker.bind(on_ok=self.on_time_selected)  
        self.time_picker.open()
        

    def on_time_selected(self, value):
        """Guarda la hora seleccionada y la muestra en el campo de texto que la llamó."""
        time_str = f"{value.time}" 
        # Convertir el tiempo de formato HH:MM:SS a HH:MM
        hora_minutos = time_str.split(":")[:2]  # Extrae solo la hora y los minutos
        time_str = ":".join(hora_minutos)
        
        if self.caller:
            self.caller.text = time_str  # Actualiza el campo de texto del caller
            
        self.time_picker.dismiss()