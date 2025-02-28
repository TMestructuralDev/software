from kivymd.uix.screen import MDScreen
from utils.auth import login_user
from kivymd.toast import toast



class LoginScreen(MDScreen):
    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text
        
        if not username or not password:
            toast("Por favor ingrese usuario y contraseña")
            return

        response = login_user(username, password)

        if response["success"]:
            self.manager.get_screen("home_screen").token = response["token"]
            self.manager.current = "home_screen"
        else:
            toast("Error en login, verifique sus credenciales")