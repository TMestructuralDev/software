from kivymd.uix.pickers import MDModalDatePicker
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

class DatePicker(MDBoxLayout):  # Cambiado de MDScreen a MDBoxLayout para ser usado como widget
    fecha = StringProperty("")  

    def show_date_picker(self, caller):
        """Abre el selector de fecha y actualiza el campo de texto."""
        self.caller = caller  
        self.date_picker = MDModalDatePicker()      
        self.date_picker.bind(on_ok=self.on_date_selected)
        self.date_picker.open()

    def on_date_selected(self, value):
        """Guarda la fecha seleccionada y la muestra en el campo de texto que la llamó."""
        selected_date = value.get_date()[0]  
        self.fecha = f"{selected_date.day:02d}/{selected_date.month:02d}/{selected_date.year}"

        if self.caller:
            self.caller.text = self.fecha  # Actualiza el campo de fecha
            
        self.date_picker.dismiss()
