from utilidades.utilidades import Utilidades
import prettytable as pt
from Controller.controlador import Controlador
from Controller.controlador import ControladorDestino, ControladorPaqueteTuristico, ControladorReserva
from models.usuario import UsuarioModelo
from datetime import datetime
import time


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