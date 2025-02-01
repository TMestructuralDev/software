from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import MainScreen
from screens.estructural_screen import EstructuralScreen
from screens.gruas_screen import GruasScreen
from screens.notas_gruas_screen import NotaGruasScreen

class NavigationController(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainScreen(name="main"))  # <- Pantalla principal
        self.add_widget(EstructuralScreen(name="estructural"))
        self.add_widget(GruasScreen(name="gruas"))
        self.add_widget(NotaGruasScreen(name="nota_gruas"))

        self.current = "main"  # <- IMPORTANTE: Esto asegura que se muestre MainScreen