from utilidades.utilidades import Utilidades
from controlador import Controlador

class MenuPrincipal:
    def __init__(self):
        pass

    def menu(self):
        while True:
            Utilidades.limpiar_pantalla()
            print("--- Menu Principal ---\n")
            print("1. Iniciar Sesion")
            print("2. Registrarse")
            print("S. Salir")
            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                self.iniciar_sesion()
            elif opcion == '2':
                self.registrarse()
            elif opcion.lower() == 's':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def iniciar_sesion(self):
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        if Controlador.iniciar_sesion(usuario, contrasena):
            print("Inicio de sesión exitoso.")
            Utilidades.pausar()
            
        else:
            print("Usuario o contraseña incorrectos. Intente de nuevo.")
            Utilidades.pausar()

    def registrarse(self):
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        confirmar_contrasena = input("Confirme su contraseña: ")
        
        success, message = Controlador.registrarse(usuario, contrasena, confirmar_contrasena)
        print(message)
        Utilidades.pausar()
        if not success:
            return

if __name__ == '__main__':
    menu_principal = MenuPrincipal()
    menu_principal.menu()



