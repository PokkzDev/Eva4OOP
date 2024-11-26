from utilidades.utilidades import Utilidades
from controlador import Controlador
import prettytable as pt
from controlador import ControladorDestino, ControladorPaqueteTuristico
from datetime import datetime

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

            if usuario == 'admin':
                menu = MenuAdmin()
                menu.mostrar_menu()
            else:
                pass
            
        else:
            print("Usuario o contraseña incorrectos. Intente de nuevo.")
            Utilidades.pausar()

    def registrarse(self):
        Utilidades.en_desarrollo()
    

class MenuAdmin:
    def __init__(self):
        pass

    def mostrar_menu(self):
        while True:
            Utilidades.limpiar_pantalla()
            print("--- Menu Admin ---\n")

            opciones =[
                "1. Menu Destinos Turisticos",
                "2. Menu Paquetes Turisticos",
                "S. Salir"
            ]

            for opcion in opciones:
                print(opcion)
            
            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                self.menu_destinos_turisticos()
            elif opcion == '2':
                self.menu_paquetes()
            elif opcion.lower() == 's':
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                Utilidades.pausar()

    def menu_destinos_turisticos(self):
        controlador_destino = ControladorDestino()

        def obtener_destinos():
            destinos = controlador_destino.obtener_destinos()
            table = pt.PrettyTable()
            table.field_names = ["ID", "Nombre", "Descripción", "Actividades", "Costo"]
            for destino in destinos:
                table.add_row(destino)
            return table

        while True:
            Utilidades.limpiar_pantalla()
            print("--- Menu Destinos Turisticos ---\n")

            opciones = [
                "1. Ver destinos turisticos",
                "2. Agregar destino turistico",
                "3. Modificar destino turistico",
                "4. Eliminar destino turistico",
                "S. Salir"
            ]

            for opcion in opciones:
                print(opcion)
            
            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                Utilidades.limpiar_pantalla()
                print("--- Destinos Turisticos ---\n")
                print(obtener_destinos())
                Utilidades.pausar()
            elif opcion == '2':
                Utilidades.limpiar_pantalla()
                print("--- Agregar Destino Turistico ---\n")
                nombre = input("Ingrese el nombre del destino: ")
                descripcion = input("Ingrese la descripción del destino: ")
                actividades = input("Ingrese las actividades del destino: ")
                costo = input("Ingrese el costo del destino: ")

                if not nombre or not descripcion or not actividades or not costo:
                    print("Todos los campos son obligatorios. Intente de nuevo.")
                    Utilidades.pausar()
                    continue

                if controlador_destino.crear_destino(nombre, descripcion, actividades, costo):
                    print("Destino agregado exitosamente.")
                else:
                    print("Error al agregar el destino.")
                Utilidades.pausar()
            elif opcion == '3':
                Utilidades.limpiar_pantalla()
                print("--- Modificar Destino Turistico ---\n")
                print(obtener_destinos())
                id_destino = input("Ingrese el ID del destino a modificar: ")
                destino = controlador_destino.obtener_destino(id_destino)
                if not destino:
                    print("Destino no encontrado.")
                    Utilidades.pausar()
                    continue
                nombre = input(f"Ingrese el nuevo nombre del destino [{destino[1]}]: ") or destino[1]
                descripcion = input(f"Ingrese la nueva descripción del destino [{destino[2]}]: ") or destino[2]
                actividades = input(f"Ingrese las nuevas actividades del destino [{destino[3]}]: ") or destino[3]
                costo = input(f"Ingrese el nuevo costo del destino [{destino[4]}]: ") or destino[4]
                if controlador_destino.actualizar_destino(id_destino, nombre, descripcion, actividades, costo):
                    print("Destino modificado exitosamente.")
                else:
                    print("Error al modificar el destino.")
                Utilidades.pausar()
            elif opcion == '4':
                Utilidades.limpiar_pantalla()
                print("--- Eliminar Destino Turistico ---\n")
                print(obtener_destinos())
                id_destino = input("Ingrese el ID del destino a eliminar: ")
                if controlador_destino.eliminar_destino(id_destino):
                    print("Destino eliminado exitosamente.")
                else:
                    print("Error al eliminar el destino.")
                Utilidades.pausar()
            elif opcion.lower() == 's':
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                Utilidades.pausar()
        controlador_destino.cerrar_conexion()
    
    def menu_paquetes(self):
        controlador_paquete = ControladorPaqueteTuristico()
        controlador_destino = ControladorDestino()

        def obtener_paquetes():
            paquetes = controlador_paquete.obtener_paquetes_turisticos()
            table = pt.PrettyTable()
            table.field_names = ["ID", "Fecha Inicio", "Fecha Fin", "Precio Total", "Destinos"]
            for paquete in paquetes:
                table.add_row(paquete)
            return table
        while True:
            Utilidades.limpiar_pantalla()
            print("--- Menu Paquetes Turisticos ---\n")

            opciones = [
                "1. Ver paquetes turisticos",
                "2. Agregar paquete turistico",
                "3. Modificar paquete turistico",
                "4. Eliminar paquete turistico",
                "S. Salir"
            ]

            for opcion in opciones:
                print(opcion)
            
            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                Utilidades.limpiar_pantalla()
                print("--- Paquetes Turisticos ---\n")
                print(obtener_paquetes())
                Utilidades.pausar()
            elif opcion == '2':
                Utilidades.limpiar_pantalla()
                print("--- Agregar Paquete Turistico ---\n")
                fecha_inicio = input("Ingrese la fecha de inicio (DD-MM-YYYY): ")
                fecha_fin = input("Ingrese la fecha de fin (DD-MM-YYYY): ")
                
                try:
                    fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y").strftime("%Y-%m-%d")
                    fecha_fin = datetime.strptime(fecha_fin, "%d-%m-%Y").strftime("%Y-%m-%d")
                except ValueError:
                    print("Formato de fecha inválido.")
                    Utilidades.pausar()
                    continue

                # Seleccionar destinos
                destinos = controlador_destino.obtener_destinos()
                if not destinos:
                    print("No hay destinos disponibles para agregar.")
                    Utilidades.pausar()
                    continue
                print("Seleccione destinos por ID separados por comas:")
                for destino in destinos:
                    print(f"{destino[0]}. {destino[1]} - {destino[4]}")
                seleccion = input("Ingrese los IDs de los destinos: ")
                try:
                    destino_ids = [int(id.strip()) for id in seleccion.split(',')]
                except ValueError:
                    print("Selección inválida de destinos.")
                    Utilidades.pausar()
                    continue

                if controlador_paquete.crear_paquete_turistico(fecha_inicio, fecha_fin, destino_ids):
                    print("Paquete turistico agregado exitosamente.")
                else:
                    print("Error al agregar el paquete turistico.")
                Utilidades.pausar()
            elif opcion == '3':
                Utilidades.limpiar_pantalla()
                print("--- Modificar Paquete Turistico ---\n")
                print(obtener_paquetes())
                id_paquete = input("Ingrese el ID del paquete a modificar: ")
                paquete = controlador_paquete.obtener_paquete_turistico(id_paquete)
                if not paquete:
                    print("Paquete no encontrado.")
                    Utilidades.pausar()
                    continue
                fecha_inicio = input(f"Ingrese la nueva fecha de inicio (DD-MM-YYYY) [{paquete[1]}]: ")
                fecha_fin = input(f"Ingrese la nueva fecha de fin (DD-MM-YYYY) [{paquete[2]}]: ")
                
                try:
                    if fecha_inicio:
                        fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y").strftime("%Y-%m-%d")
                    else:
                        fecha_inicio = paquete[1]
                    
                    if fecha_fin:
                        fecha_fin = datetime.strptime(fecha_fin, "%d-%m-%Y").strftime("%Y-%m-%d")
                    else:
                        fecha_fin = paquete[2]
                except ValueError:
                    print("Formato de fecha inválido.")
                    Utilidades.pausar()
                    continue

                # Seleccionar nuevos destinos
                destinos = controlador_destino.obtener_destinos()
                if not destinos:
                    print("No hay destinos disponibles para agregar.")
                    Utilidades.pausar()
                    continue
                print("Seleccione nuevos destinos por ID separados por comas:")
                for destino in destinos:
                    print(f"{destino[0]}. {destino[1]} - {destino[4]}")
                seleccion = input("Ingrese los IDs de los destinos: ")
                try:
                    destino_ids = [int(id.strip()) for id in seleccion.split(',')]
                except ValueError:
                    print("Selección inválida de destinos.")
                    Utilidades.pausar()
                    continue

                precio_total = None  # Will be calculated automatically
                if controlador_paquete.actualizar_paquete_turistico(id_paquete, fecha_inicio, fecha_fin, destino_ids):
                    print("Paquete turistico modificado exitosamente.")
                else:
                    print("Error al modificar el paquete turistico.")
                Utilidades.pausar()
            elif opcion == '4':
                Utilidades.limpiar_pantalla()
                print("--- Eliminar Paquete Turistico ---\n")
                print(obtener_paquetes())
                id_paquete = input("Ingrese el ID del paquete a eliminar: ")
                if controlador_paquete.eliminar_paquete_turistico(id_paquete):
                    print("Paquete turistico eliminado exitosamente.")
                else:
                    print("Error al eliminar el paquete turistico.")
                Utilidades.pausar()
            elif opcion.lower() == 's':
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                Utilidades.pausar()
        controlador_paquete.cerrar_conexion()
        controlador_destino.cerrar_conexion()

if __name__ == '__main__':
    # bypass and test admin menu
    menu = MenuAdmin()
    menu.mostrar_menu()



