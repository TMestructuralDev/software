from kivy.lang import Builder
from kivymd.app import MDApp
from controllers.nav_controller import NavigationController

class MyApp(MDApp):
    def build(self):
        Builder.load_file("kv/main.kv")  # Asegúrate de que el archivo KV se cargue correctamente
        return NavigationController()

if __name__ == "__main__":
    MyApp().run()