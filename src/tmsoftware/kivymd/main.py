from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
import requests

KV = '''
MDScreen:
    MDTextField:
        id: username_input
        hint_text: "Username"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: 0.8, None
        height: "40dp"
    
    MDTextField:
        id: password_input
        hint_text: "Password"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: 0.8, None
        height: "40dp"
        password: True
    
    MDRaisedButton:
        text: "Login"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        size_hint: 0.5, None
        height: "50dp"
        on_release: app.login()
'''

class LoginScreen(MDScreen):
    pass

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def login(self):
        # Obtener datos de los campos
        username = self.root.ids.username_input.text
        password = self.root.ids.password_input.text

        # URL de la API para login
        url = "http://127.0.0.1:8000/api/login/"  # Cambia según sea necesario

        # Crear el diccionario con los datos
        data = {
            'username': username,
            'password': password
        }

        # Hacer la solicitud POST
        response = requests.post(url, data=data)

        if response.status_code == 200:
            print("Login exitoso")
        else:
            print("Error en el login")

if __name__ == "__main__":
    MainApp().run()