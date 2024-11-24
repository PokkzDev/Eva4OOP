import sqlite3
import bcrypt
import pwinput
import os

class AdministracionUsuarios:
    def __init__(self, db_path='./baseDeDatos/viajes_aventura.db'):
        self.db_path = db_path

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

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Usuarios (nombre, contrasena, rol)
            VALUES (?, ?, ?)
        ''', (nombre, hashed_password, rol))

        conn.commit()
        conn.close()

        print("Usuario creado exitosamente.")

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nMenu de Usuarios")
            print("1. Crear usuario")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.create_user()
            elif opcion == '2':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    user_manager = AdministracionUsuarios()
    user_manager.menu()
