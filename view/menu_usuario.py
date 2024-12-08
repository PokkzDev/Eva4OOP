from utilidades.utilidades import Utilidades
import prettytable as pt
from Controller.controlador import Controlador
from Controller.controlador_paquete_turistico import ControladorPaqueteTuristico
from Controller.controlador_reserva import ControladorReserva
from datetime import datetime



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
                print("Volviendo al inicio de sesión...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                Utilidades.pausar()

    def ver_paquetes_turisticos(self):
        controlador_paquete = ControladorPaqueteTuristico()
        paquetes = controlador_paquete.obtener_paquetes_turisticos()
        table = pt.PrettyTable()
        table.field_names = ["ID", "Fecha Inicio", "Fecha Fin", "Precio Total", "Destinos"]
        # Asegúrate de agregar solo los valores correctos a la tabla
        for paquete in paquetes:
            # Extraemos los valores del diccionario
            table.add_row([paquete['id'], paquete['fecha_inicio'], paquete['fecha_fin'], paquete['precio_total'], paquete['destinos']])
        print(table)
        Utilidades.pausar()
        controlador_paquete.cerrar_conexion()

    def buscar_paquetes_por_rango_fechas(self):  
        controlador_paquete = ControladorPaqueteTuristico()
        # Convertir las fechas del formato 'DD-MM-YYYY' a 'YYYY-MM-DD'
        while True:
            try:
                # Solicitar la fecha de inicio
                fecha_inicio = input("Ingrese la fecha de inicio (DD-MM-YYYY): ")
                # Intentar convertir la fecha al formato adecuado
                fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y").strftime("%Y-%m-%d")
                break  # Si la conversión es exitosa, salir del bucle
            except ValueError:
                print("El formato de la fecha de inicio es incorrecto. Por favor, ingrese la fecha en formato DD-MM-YYYY.")

        while True:
            try:
                # Solicitar la fecha de fin
                fecha_fin = input("Ingrese la fecha de fin (DD-MM-YYYY): ")
                # Intentar convertir la fecha al formato adecuado
                fecha_fin = datetime.strptime(fecha_fin, "%d-%m-%Y").strftime("%Y-%m-%d")
                break  # Si la conversión es exitosa, salir del bucle
            except ValueError:
                print("El formato de la fecha de fin es incorrecto. Por favor, ingrese la fecha en formato DD-MM-YYYY.")
        paquetes = controlador_paquete.buscar_paquete_turistico_por_rango_fechas(fecha_inicio, fecha_fin)
        table = pt.PrettyTable()
        table.field_names = ["ID", "Fecha Inicio", "Fecha Fin", "Precio Total", "Destinos", "Actividades"]
        # Asegúrate de agregar solo los valores correctos a la tabla
        for paquete in paquetes:
            # Extraemos los valores del diccionario
            table.add_row([paquete['id'], paquete['fecha_inicio'], paquete['fecha_fin'], paquete['precio_total'], paquete['destinos'], paquete['actividades']])
        print(table)
        Utilidades.pausar()
        controlador_paquete.cerrar_conexion()

    def reservar_paquete_turistico(self):
        controlador_usuario = Controlador()
        usuario = controlador_usuario.obtener_usuario_por_id(self.usuario_id)
        if not usuario.get_hasDatosPersonales(): 
            print("Debe completar sus datos personales antes de realizar una reserva.")
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            while True:
                try:
                    # Solicitar la fecha de fin
                    fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD-MM-YYYY): ")
                    # Intentar convertir la fecha al formato adecuado
                    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y").strftime("%Y-%m-%d")
                    break  # Si la conversión es exitosa, salir del bucle
                except ValueError:
                    print("El formato de la fecha de nacimiento es incorrecto. Por favor, ingrese la fecha en formato DD-MM-YYYY.")
            direccion = input("Ingrese su dirección: ")
            telefono = input("Ingrese su teléfono: ")
            if controlador_usuario.agregar_datos_personales(self.usuario_id, nombre, apellido, fecha_nacimiento, direccion, telefono):
                print("Datos personales agregados exitosamente.")
            else:
                print("Error al agregar los datos personales.")
                Utilidades.pausar()
                return
        controlador_paquete = ControladorPaqueteTuristico()
        controlador_reserva = ControladorReserva()
        paquetes = controlador_paquete.obtener_paquetes_turisticos()
        table = pt.PrettyTable()
        table.field_names = ["ID", "Fecha Inicio", "Fecha Fin", "Precio Total", "Destinos"]
        for paquete in paquetes:
            table.add_row([paquete['id'], paquete['fecha_inicio'], paquete['fecha_fin'], paquete['precio_total'], paquete['destinos']])
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
        if any(reserva['paquete_id'] == int(id_paquete) for reserva in reservas):
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
            paquete_id = reserva['paquete_id']
            controlador_paquete = ControladorPaqueteTuristico()
            paquete = controlador_paquete.obtener_paquete_turistico(paquete_id)
            destinos = controlador_paquete.obtener_destinos_de_paquete(paquete_id)
            destinos_str = ",\n".join([destino['nombre'] for destino in destinos])
            actividades_str = ",\n".join([destino['actividades'] for destino in destinos])
            table.add_row([reserva['id'], reserva['fecha_fin'], paquete['fecha_inicio'], paquete['fecha_fin'], paquete['precio_total'], destinos_str, actividades_str])
            controlador_paquete.cerrar_conexion()
        print(table)
        Utilidades.pausar()
        controlador_reserva.cerrar_conexion()



    def cancelar_reserva(self):  
        controlador_reserva = ControladorReserva()
        reservas = controlador_reserva.obtener_reservas_por_usuario(self.usuario_id)    
        table = pt.PrettyTable()
        table.field_names = ["ID Reserva", "Fecha Reserva", "Fecha Inicio", "Fecha Fin", "Precio Total", "Destinos", "Actividades"]
        for reserva in reservas:
            paquete_id = reserva['paquete_id']
            controlador_paquete = ControladorPaqueteTuristico()
            paquete = controlador_paquete.obtener_paquete_turistico(paquete_id)
            destinos = controlador_paquete.obtener_destinos_de_paquete(paquete_id)
            destinos_str = ",\n".join([destino['nombre'] for destino in destinos])
            actividades_str = ",\n".join([destino['actividades'] for destino in destinos])
            table.add_row([reserva['id'], reserva['fecha_reserva'], paquete['fecha_inicio'], paquete['fecha_fin'], paquete['precio_total'], destinos_str, actividades_str])
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