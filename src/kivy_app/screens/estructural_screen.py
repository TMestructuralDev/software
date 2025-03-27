from kivymd.uix.screen import MDScreen
from widgets.date_picker import DatePicker
from kivy.properties import StringProperty


class EstructuralScreen(MDScreen):
    
    fecha = StringProperty("") 
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date_picker = DatePicker()
        
    def open_date_picker(self, field):
        """Llama al DatePicker y pasa el campo de texto que lo activó."""
        self.date_picker.show_date_picker(field)