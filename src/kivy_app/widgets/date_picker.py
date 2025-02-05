from kivymd.uix.pickers import MDDatePicker
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

class DatePicker(MDBoxLayout):  # Cambiado de MDScreen a MDBoxLayout para ser usado como widget
    selected_date = StringProperty("")

    def show_date_picker(self, caller):
        """Abre el selector de fecha y actualiza el campo de texto."""
        self.caller = caller  # Guardamos quién llamó al selector
        date_picker = MDDatePicker()
        date_picker.bind(on_save=self.on_date_selected)
        date_picker.open()

    def on_date_selected(self, instance, value, date_range):
        """Guarda la fecha seleccionada y la muestra en el campo de texto que la llamó."""
        self.selected_date = str(value)
        if self.caller:
            self.caller.text = self.selected_date  # Actualiza el campo de te