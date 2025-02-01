from kivymd.uix.screen import MDScreen

class MainScreen(MDScreen):
    def go_to_estructural(self):
        self.manager.current = "estructural"

    def go_to_gruas(self):
        self.manager.current = "gruas"