from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.notas_gruas_screen import NotaGruasScreen
from screens.estructural_screen import EstructuralScreen
from screens.login_screen import LoginScreen

class NavigationController(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HomeScreen(name="home_screen"))  # <- Pantalla principal
        self.add_widget(EstructuralScreen(name="estructural_screen"))
        self.add_widget(NotaGruasScreen(name="notas_gruas_screen"))
        self.add_widget(LoginScreen(name="login_screen"))


        #self.current = "login_screen"  # <- IMPORTANTE: Esto asegura que se muestre MainScreen.
        self.current = "home_screen"  # <- IMPORTANTE: Pantalla para testeo.