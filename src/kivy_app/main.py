from kivy.lang import Builder
from kivymd.app import MDApp
from controllers.nav_controller import NavigationController

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark" 
        #self.theme_cls.primary_palette = "Orange"  # Si no quieres usar naranja, cámbialo a otro color
        
        Builder.load_file("kv/home.kv")  # Se carga el archivo KV 
        Builder.load_file("kv/notas_gruas.kv")
        Builder.load_file("kv/estructural.kv")
        Builder.load_file("kv/login.kv")
        
        return NavigationController()

if __name__ == "__main__":
    MyApp().run()