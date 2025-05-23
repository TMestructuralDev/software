from kivy.lang import Builder
from kivymd.app import MDApp
from controllers.nav_controller import NavigationController
from kivy.core.window import Window
import os

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "Orange" 
        self.theme_cls.material_style = "M3" 
        Window.softinput_mode = "pan" 
        #Window.borderless = True
        
        # Asegúrate de que los archivos .kv se carguen correctamente incluso cuando se empaqueten.
        kv_dir = os.path.join(os.path.dirname(__file__), 'kv')
        
        # Cargar los archivos .kv
        Builder.load_file(os.path.join(kv_dir, 'home.kv'))
        Builder.load_file(os.path.join(kv_dir, 'notas_gruas.kv'))
        Builder.load_file(os.path.join(kv_dir, 'estructural.kv'))
        Builder.load_file(os.path.join(kv_dir, 'login.kv'))
        
        return NavigationController()

if __name__ == "__main__":
    MyApp().run()