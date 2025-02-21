from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.notas_gruas_screen import NotaGruasScreen
from screens.estructural_screen import EstructuralScreen
from kivy.graphics import Color, Rectangle

class NavigationController(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HomeScreen(name="home"))  # <- Pantalla principal
        self.add_widget(EstructuralScreen(name="estructural_screen"))
        self.add_widget(NotaGruasScreen(name="notas_gruas_screen"))

        self.current = "home"  # <- IMPORTANTE: Esto asegura que se muestre MainScreen