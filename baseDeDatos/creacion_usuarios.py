import bcrypt
import pwinput
import os
from baseDeDatos.db_conn import DBConn

class AdministracionUsuarios:
    def __init__(self):
        self.db = DBConn()

    def create_user(self):
        nombre = input("Ingrese el nombre del usuario: ")
        
        while True:
            contrasena = pwinput.pwinput(prompt='Ingrese la contraseña del usuario: ')
            confirm_contrasena = pwinput.pwinput(prompt='Confirme la contraseña del usuario: ')
            if contrasena == confirm_contrasena:
                break
            else:
                print("Las contraseñas no coinciden. Intente de nuevo.")

        rol = input("Ingrese el rol del usuario (admin/cliente): ")

        hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt(10))

        print("Creando usuario...")
        print("Nombre:", nombre)
        print("Contraseña:", contrasena)
        print("Rol:", rol)

        input("Presione Enter para continuar...")
        self.db.execute('''
            INSERT INTO Usuarios (username, password, rol)
            VALUES (%s, %s, %s)
        ''', (nombre, hashed_password, rol))

        print("Usuario creado exitosamente.")
        

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nMenu de Usuarios")
            print("1. Crear usuario")
            print("S. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.create_user()
            elif opcion.lower() == 's':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    user_manager = AdministracionUsuarios()
    user_manager.menu()
