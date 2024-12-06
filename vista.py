from utilidades.utilidades import Utilidades #Importación de carpeta utilidades y módulo utilidades
from Controller.controlador import Controlador #Importación de módulos
import prettytable as pt # Para crear tablas
from Controller.controlador_destino import ControladorDestino
from Controller.controlador_paquete_turistico import ControladorPaqueteTuristico
from Controller.controlador_reserva import ControladorReserva
from models.modelo import UsuarioModelo  # Importación de módulos
from datetime import datetime # Biblioteca para trabajar con fechas y horas
import pwinput # Biblioteca para ocultar contraseñas

class MenuPrincipal: 
    def __init__(self): # Constructor, inicializa la clase MenuPrincipal
        pass # No ejecuta ninguna operación

    def menu(self): 
        while True:
            Utilidades.limpiar_pantalla()  # Limpiador de pantalla al momento de mostrar nuevamente el menu
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
        Utilidades.limpiar_pantalla()
        usuario = input("Ingrese su usuario: ") # Entrada del nombre del usuario
        contrasena = pwinput.pwinput("Ingrese su contraseña: ", mask='*') # Entrada de la contraseña del usuario ocultada con *
        if Controlador.iniciar_sesion(usuario, contrasena): # verificación, cuando la condición es verdadera se muestra el mensaje "Inicio de sesión exitoso"
            print("Inicio de sesión exitoso.")
            Utilidades.pausar() # Pausa la ejecución del programa
            if usuario == 'admin': # Si la condición es verdadera se crea una instancia de la clase MenuAdmin
                menu = MenuAdmin()  
                menu.mostrar_menu() # Llama al método mostrar_menu de la instancia menu creada
            else:
                usuario_id = Controlador.obtener_id_usuario(usuario)  # Cuando la condición no se cumple se obtiene el id del usuario
                menu = MenuUsuario(usuario_id) 
                menu.mostrar_menu() # Llama al método
            
        else:
            print("Usuario o contraseña incorrectos. Intente de nuevo.")
            Utilidades.pausar()

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




class MenuUsuario:
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id

    def mostrar_menu(self):
        while True:
            Utilidades.limpiar_pantalla()
            print("--- Menu Usuario ---\n")
            print("1. Ver Paquetes Turisticos Disponibles")
            print("2. Buscar Paquetes por Rango de Fechas")
            print("3. Reservar Paquete Turistico")
            print("4. Ver Reservas")
            print("5. Cancelar Reserva")  # Add this line
            print("S. Salir")
            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                self.ver_paquetes_turisticos()
            elif opcion == '2':
                self.buscar_paquetes_por_rango_fechas()
            elif opcion == '3':
                self.reservar_paquete_turistico()
            elif opcion == '4':  
                self.ver_reservas()
            elif opcion == '5':  # Add this block
                self.cancelar_reserva()
            elif opcion.lower() == 's':
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                Utilidades.pausar()

    def ver_paquetes_turisticos(self):
        controlador_paquete = ControladorPaqueteTuristico()
        paquetes = controlador_paquete.obtener_paquetes_turisticos()
        table = pt.PrettyTable()
        table.field_names = ["ID", "Fecha Inicio", "Fecha Fin", "Precio Total", "Destinos"]
        for paquete in paquetes:
            table.add_row(paquete)
        print(table)
        Utilidades.pausar()
        controlador_paquete.cerrar_conexion()

    def reservar_paquete_turistico(self):
        controlador_usuario = Controlador()
        usuario_modelo = UsuarioModelo()
        usuario = usuario_modelo.obtener_usuario_por_id(self.usuario_id)
        if not usuario[3]: 
            print("Debe completar sus datos personales antes de realizar una reserva.")
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
            direccion = input("Ingrese su dirección: ")
            telefono = input("Ingrese su teléfono: ")
            if controlador_usuario.agregar_datos_personales(self.usuario_id, nombre, apellido, fecha_nacimiento, direccion, telefono):
                print("Datos personales agregados exitosamente.")
            else:
                print("Error al agregar los datos personales.")
                Utilidades.pausar()
                return
        usuario_modelo.cerrar_conexion()

        controlador_paquete = ControladorPaqueteTuristico()
        controlador_reserva = ControladorReserva()
        paquetes = controlador_paquete.obtener_paquetes_turisticos()
        table = pt.PrettyTable()
        table.field_names = ["ID", "Fecha Inicio", "Fecha Fin", "Precio Total", "Destinos"]
        for paquete in paquetes:
            table.add_row(paquete)
        print(table)
        id_paquete = input("Ingrese el ID del paquete a reservar: ")

        if not id_paquete.strip():  # Check for empty input
            print("No se ingresó ningún ID de paquete. Operación cancelada.")
            Utilidades.pausar()
            controlador_paquete.cerrar_conexion()
            controlador_reserva.cerrar_conexion()
            return

        # Check if the user has already reserved this package
        reservas = controlador_reserva.obtener_reservas_por_usuario(self.usuario_id)
        if any(reserva[2] == int(id_paquete) for reserva in reservas):
            print("Ya ha reservado este paquete anteriormente.")
            Utilidades.pausar()
            controlador_paquete.cerrar_conexion()
            controlador_reserva.cerrar_conexion()
            return

        fecha_reserva = datetime.now().strftime("%Y-%m-%d")
        if controlador_reserva.crear_reserva(self.usuario_id, id_paquete, fecha_reserva):
            print("Reserva realizada exitosamente.")
        else:
            print("Error al realizar la reserva.")
        Utilidades.pausar()
        controlador_paquete.cerrar_conexion()
        controlador_reserva.cerrar_conexion()

    def ver_reservas(self):
        controlador_reserva = ControladorReserva()
        reservas = controlador_reserva.obtener_reservas_por_usuario(self.usuario_id)
        table = pt.PrettyTable()
        table.field_names = ["ID Reserva", "Fecha Reserva", "Fecha Inicio", "Fecha Fin", "Precio Total", "Destinos", "Actividades"]
        for reserva in reservas:
            paquete_id = reserva[2]
            controlador_paquete = ControladorPaqueteTuristico()
            paquete = controlador_paquete.obtener_paquete_turistico(paquete_id)
            destinos = controlador_paquete.obtener_destinos_de_paquete(paquete_id)
            destinos_str = ",\n".join([destino[1] for destino in destinos])
            actividades_str = ",\n".join([destino[3] for destino in destinos])
            table.add_row([reserva[0], reserva[3], paquete[1], paquete[2], paquete[3], destinos_str, actividades_str])
            controlador_paquete.cerrar_conexion()
        print(table)
        Utilidades.pausar()
        controlador_reserva.cerrar_conexion()

    def buscar_paquetes_por_rango_fechas(self):  # Add this method
        controlador_paquete = ControladorPaqueteTuristico()
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
        paquetes = controlador_paquete.buscar_paquete_turistico_por_rango_fechas(fecha_inicio, fecha_fin)
        table = pt.PrettyTable()
        table.field_names = ["ID", "Fecha Inicio", "Fecha Fin", "Precio Total", "Destinos", "Actividades"]
        for paquete in paquetes:
            table.add_row(paquete)
        print(table)
        Utilidades.pausar()
        controlador_paquete.cerrar_conexion()

    def cancelar_reserva(self):  # Add this method
        controlador_reserva = ControladorReserva()
        reservas = controlador_reserva.obtener_reservas_por_usuario(self.usuario_id)
        table = pt.PrettyTable()
        table.field_names = ["ID Reserva", "Fecha Reserva", "Fecha Inicio", "Fecha Fin", "Precio Total", "Destinos", "Actividades"]
        for reserva in reservas:
            paquete_id = reserva[2]
            controlador_paquete = ControladorPaqueteTuristico()
            paquete = controlador_paquete.obtener_paquete_turistico(paquete_id)
            destinos = controlador_paquete.obtener_destinos_de_paquete(paquete_id)
            destinos_str = ",\n".join([destino[1] for destino in destinos])
            actividades_str = ",\n".join([destino[3] for destino in destinos])
            table.add_row([reserva[0], reserva[3], paquete[1], paquete[2], paquete[3], destinos_str, actividades_str])
            controlador_paquete.cerrar_conexion()
        print(table)
        id_reserva = input("Ingrese el ID de la reserva a cancelar: ")

        if not id_reserva.strip():  # Check for empty input
            print("No se ingresó ningún ID de reserva. Operación cancelada.")
            Utilidades.pausar()
            controlador_reserva.cerrar_conexion()
            return

        if controlador_reserva.eliminar_reserva(int(id_reserva)):
            print("Reserva cancelada exitosamente.")
        else:
            print("Error al cancelar la reserva.")
        Utilidades.pausar()
        controlador_reserva.cerrar_conexion()

if __name__ == '__main__':
    # bypass and test admin menu
    menu = MenuAdmin()
    menu.mostrar_menu()
