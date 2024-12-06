from utilidades.utilidades import Utilidades
from Controller.controlador import Controlador
from .menu_admin import MenuAdmin
from .menu_usuario import MenuUsuario
import pwinput
import time

class MenuPrincipal:
    def __init__(self):
        pass

    def mostrar_menu(self):
        while True:
            Utilidades.limpiar_pantalla()
            print("--- Menu Inicio de Sesión ---\n")
            print("1. Iniciar Sesion")
            print("2. Registrarse")
            print("S. Salir")
            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                self.iniciar_sesion()
                time.sleep(0.75)
            elif opcion == '2':
                usuario = input("ingrese usuario: ")
                cont = pwinput.pwinput("Ingrese contraseña: ", mask="*")
                Controlador.registrarse(usuario, cont)
                time.sleep(0.75)
            elif opcion.lower() == 's':
                print("Hasta pronto!!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                time.sleep(0.75)

    def iniciar_sesion(self):
        Utilidades.limpiar_pantalla()
        usuario = input("Ingrese su usuario: ")
        contrasena = pwinput.pwinput("Ingrese su contraseña: ", mask='*')
        user = Controlador.iniciar_sesion(usuario, contrasena)
        if user:
            print("Inicio de sesión exitoso.")
            time.sleep(0.75)
            if user.get_rol() == 'admin':
                menu = MenuAdmin()
                menu.mostrar_menu()
            elif user.get_rol() == 'cliente':
                usuario_id = Controlador.obtener_id_usuario(usuario)
                menu = MenuUsuario(usuario_id)
                menu.mostrar_menu()
            else:
                print("Rol desconocido. No se puede acceder al sistema.")
            time.sleep(1)
            
        else:
            print("Usuario o contraseña incorrectos. Intente de nuevo.")
            time.sleep(0.75)

    def registrarse(self):
        Utilidades.limpiar_pantalla()
        print("--- Registro de Usuario ---\n")
        usuario = input("Ingrese su usuario: ")
        while True:
            contrasena = pwinput.pwinput("Ingrese su contraseña: ", mask='*')
            confirm_contrasena = pwinput.pwinput("Confirme su contraseña: ", mask='*')
            if contrasena == confirm_contrasena:
                break
            else:
                print("Las contraseñas no coinciden. Intente de nuevo.")
        
        if Controlador.registrarse(usuario, contrasena):
            print("Usuario registrado exitosamente.")
        else:
            print("Error al registrar el usuario. Intente de nuevo.")
        Utilidades.pausar()



if __name__ == '__main__':
    # bypass and test admin menu
    menu = MenuPrincipal()
    menu.menu()