from kivy.lang import Builder
from kivymd.app import MDApp
from controllers.nav_controller import NavigationController

class MyApp(MDApp):
    def build(self):
        Builder.load_file("kv/home.kv")  # Asegúrate de que el archivo KV se cargue correctamente
        Builder.load_file("kv/notas_gruas.kv")
        Builder.load_file("kv/estructural.kv")
        
        return NavigationController()

if __name__ == "__main__":
    MyApp().run()