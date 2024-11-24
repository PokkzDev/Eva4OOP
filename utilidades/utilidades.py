import os

class Utilidades:
    @staticmethod
    def limpiar_pantalla():  # Changed method name to clear_screen
        os.system('cls' if os.name == 'nt' else 'clear')