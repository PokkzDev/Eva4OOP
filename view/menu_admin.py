from utilidades.utilidades import Utilidades
import prettytable as pt
from Controller.controlador import ControladorDestino, ControladorPaqueteTuristico, ControladorReserva
from datetime import datetime
import time



class MenuAdmin:
    def __init__(self):
        pass

    def mostrar_menu(self):
        while True:
            Utilidades.limpiar_pantalla()
            print("--- Menu Principal Admin ---\n")

            opciones =[
                "1. Gestionar Destinos Turisticos",
                "2. Gestionar Paquetes Turisticos",
                "S. Volver"
            ]

            for opcion in opciones:
                print(opcion)
            
            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                self.menu_destinos_turisticos()
            elif opcion == '2':
                self.menu_paquetes()
            elif opcion.lower() == 's':
                print("Volviendo al inicio de sesión...")
                time.sleep(0.75)
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                time.sleep(0.75)

    def menu_destinos_turisticos(self):
        controlador_destino = ControladorDestino()

        def obtener_destinos():
            destinos = controlador_destino.obtener_destinos()
            table = pt.PrettyTable()
            table.field_names = ["ID", "Nombre", "Descripción", "Actividades", "Costo"]
            for destino in destinos:
                # Accede a los atributos de cada instancia de Destino
                table.add_row([destino.id, destino.nombre, destino.descripcion, destino.actividades, destino.costo])
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
                    time.sleep(0.75)
                    continue

                if controlador_destino.crear_destino(nombre, descripcion, actividades, costo):
                    print("Destino agregado exitosamente.")
                else:
                    print("Error al agregar el destino.")
                time.sleep(0.75)
            elif opcion == '3':
                Utilidades.limpiar_pantalla()
                print("--- Modificar Destino Turistico ---\n")
                print(obtener_destinos())
                id_destino = input("Ingrese el ID del destino a modificar: ")
                destino = controlador_destino.obtener_destino(id_destino)
                if not destino:
                    print("Destino no encontrado.")
                    time.sleep(0.75)
                    continue
                nombre = input(f"Ingrese el nuevo nombre del destino [{destino['nombre']}]: ") or destino['nombre']
                descripcion = input(f"Ingrese la nueva descripción del destino [{destino['descripciones']}]: ") or destino['descripciones']
                actividades = input(f"Ingrese las nuevas actividades del destino [{destino['actividades']}]: ") or destino['actividades']
                costo = input(f"Ingrese el nuevo costo del destino [{destino['costo']}]: ") or destino['costo']
                if controlador_destino.actualizar_destino(id_destino, nombre, descripcion, actividades, costo):
                    print("Destino modificado exitosamente.")
                else:
                    print("Error al modificar el destino.")
                time.sleep(0.75)
            elif opcion == '4':
                Utilidades.limpiar_pantalla()
                print("--- Eliminar Destino Turistico ---\n")
                print(obtener_destinos())
                id_destino = input("Ingrese el ID del destino a eliminar: ")
                if controlador_destino.eliminar_destino(id_destino):
                    print("Destino eliminado exitosamente.")
                else:
                    print("Error al eliminar el destino.")
                time.sleep(0.75)
            elif opcion.lower() == 's':
                print("Volviendo al Menu Principal Admin...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                time.sleep(0.75)
        controlador_destino.cerrar_conexion()
    
    def menu_paquetes(self):
        controlador_paquete = ControladorPaqueteTuristico()
        controlador_destino = ControladorDestino()

        def obtener_paquetes():
            paquetes = controlador_paquete.obtener_paquetes_turisticos()
            table = pt.PrettyTable()
            table.field_names = ["ID", "Fecha Inicio", "Fecha Fin", "Precio Total", "Destinos"]
            for paquete in paquetes:
                table.add_row([paquete['id'], paquete['fecha_inicio'], paquete['fecha_fin'], paquete['precio_total'], paquete['destinos']])
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
                while True:
                    try:
                        fecha_inicio = input("Ingrese la fecha de inicio (DD-MM-YYYY): ")
                        fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y")
                        fecha_fin = input("Ingrese la fecha de fin (DD-MM-YYYY): ")
                        fecha_fin = datetime.strptime(fecha_fin, "%d-%m-%Y")
                        if fecha_inicio <= datetime.now():
                            print("La fecha de inicio debe ser posterior a la fecha actual.")
                            continue
                        elif fecha_fin <= datetime.now() or fecha_fin <= fecha_inicio:
                            print("La fecha de fin debe ser posterior a la fecha actual y a la fecha de inicio.")
                            continue
                        fecha_inicio = fecha_inicio.strftime("%Y-%m-%d")
                        fecha_fin = fecha_fin.strftime("%Y-%m-%d")
                        break
                    except ValueError:
                        print("Formato de fecha inválido.")
                        time.sleep(0.75)

                # Seleccionar destinos
                destinos = controlador_destino.obtener_destinos()
                if not destinos:
                    print("No hay destinos disponibles para agregar.")
                    time.sleep(0.75)
                    continue
                print("Seleccione destinos por ID separados por comas:")
                for destino in destinos:
                    print(f"{destino.id}. {destino.nombre} - {destino.costo}")
                seleccion = input("Ingrese los IDs de los destinos: ")
                try:
                    destino_ids = [int(id.strip()) for id in seleccion.split(',')]
                except ValueError:
                    print("Selección inválida de destinos.")
                    time.sleep(0.75)
                    continue
                
                if controlador_paquete.crear_paquete_turistico(fecha_inicio, fecha_fin, destino_ids):
                    print("Paquete turistico agregado exitosamente.")
                else:
                    print("Error al agregar el paquete turistico.")
                time.sleep(0.75)

            elif opcion == '3':
                Utilidades.limpiar_pantalla()
                print("--- Modificar Paquete Turistico ---\n")
                print(obtener_paquetes())
                id_paquete = input("Ingrese el ID del paquete a modificar: ")
                paquete = controlador_paquete.obtener_paquete_turistico(id_paquete)
                if not paquete:
                    print("Paquete no encontrado.")
                    time.sleep(0.75)
                    continue
                fecha_inicio = input(f"Ingrese la nueva fecha de inicio (DD-MM-YYYY) [{paquete['fecha_inicio']}]: ")
                fecha_fin = input(f"Ingrese la nueva fecha de fin (DD-MM-YYYY) [{paquete['fecha_fin']}]: ")
                
                try:
                    if fecha_inicio:
                        fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y").strftime("%Y-%m-%d")
                    else:
                        fecha_inicio = paquete['fecha_inicio']
                    
                    if fecha_fin:
                        fecha_fin = datetime.strptime(fecha_fin, "%d-%m-%Y").strftime("%Y-%m-%d")
                    else:
                        fecha_fin = paquete['fecha_fin']
                except ValueError:
                    print("Formato de fecha inválido.")
                    time.sleep(0.75)
                    continue

                # Seleccionar nuevos destinos
                destinos = controlador_destino.obtener_destinos()
                if not destinos:
                    print("No hay destinos disponibles para agregar.")
                    time.sleep(0.75)
                    continue
                print("Seleccione nuevos destinos por ID separados por comas:")
                for destino in destinos:
                    print(f"{destino.id}. {destino.nombre} - {destino.costo}")
                seleccion = input("Ingrese los IDs de los destinos: ")
                try:
                    destino_ids = [int(id.strip()) for id in seleccion.split(',')]
                except ValueError:
                    print("Selección inválida de destinos.")
                    time.sleep(0.75)
                    continue

                precio_total = None  # Will be calculated automatically
                if controlador_paquete.actualizar_paquete_turistico(id_paquete, fecha_inicio, fecha_fin, destino_ids):
                    print("Paquete turistico modificado exitosamente.")
                else:
                    print("Error al modificar el paquete turistico.")
                time.sleep(0.75)
            elif opcion == '4':
                Utilidades.limpiar_pantalla()
                print("--- Eliminar Paquete Turistico ---\n")
                print(obtener_paquetes())
                id_paquete = input("Ingrese el ID del paquete a eliminar: ")
                if controlador_paquete.eliminar_paquete_turistico(id_paquete):
                    print("Paquete turistico eliminado exitosamente.")
                    time.sleep(0.75)
                else:
                    print("Error al eliminar el paquete turistico.")
                    time.sleep(2)
            elif opcion.lower() == 's':
                print("Volviendo al Menu Principal Admin...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                time.sleep(0.75)
        controlador_paquete.cerrar_conexion()
        controlador_destino.cerrar_conexion()