import os

class Utilidades:
    @staticmethod
    def limpiar_pantalla():  # Changed method name to clear_screen
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pausar():
        input("Presione Enter para continuar...")

    @staticmethod
    def en_desarrollo():
        print("Esta función está en desarrollo.")
        Utilidades.pausar()