from kivymd.uix.screen import MDScreen


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def go_to_estructural(self):
        # Cambio de pantalla a la vista estructural
        self.manager.current = "estructural_screen"

    def go_to_nota_gruas(self):
        # Cambio de pantalla a la vista de notas de grúas
        self.manager.current = "notas_gruas_screen"
        