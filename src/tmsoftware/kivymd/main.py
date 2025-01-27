from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.login_button = Button(text="Login", size_hint=(None, None), size=(200, 50), pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.login_button.bind(on_press=self.login)
        self.add_widget(self.login_button)

    def login(self, instance):
        url = "http://127.0.0.1:8000/api/login/"  # Asegúrate de que esta sea la URL correcta para tu API
    data = {
        'username': 'usuario',  # Reemplaza con los datos que el usuario ingresa en los campos de texto
        'password': 'contraseña'
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Login exitoso")
    else:
        print("Error en el login")

class MyApp(MDApp):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()