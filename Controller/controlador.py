# Separalo en archivos correspondientes de cada clase este archivo en archivos distintos.

from models.usuario import UsuarioModelo
from models.destino import DestinoModelo
from models.paquete_turistico import PaqueteTuristicoModelo
from models.reservas import ReservasModelo

class Controlador:
    @staticmethod
    def iniciar_sesion(usuario, contrasena):
        usuario_modelo = UsuarioModelo()
        resultado = usuario_modelo.verificar_usuario(usuario, contrasena)
        usuario_modelo.cerrar_conexion()
        return resultado

    @staticmethod
    def registrarse(usuario, contrasena):
        usuario_modelo = UsuarioModelo()
        resultado = usuario_modelo.registrar_usuario(usuario, contrasena)
        if resultado == False:
            print("Ya existe ese nombre de usuario")
        usuario_modelo.cerrar_conexion()
        return resultado

    @staticmethod
    def agregar_datos_personales(usuario_id, nombre, apellido, fecha_nacimiento, direccion, telefono):
        usuario_modelo = UsuarioModelo()
        resultado = usuario_modelo.agregar_datos_personales(usuario_id, nombre, apellido, fecha_nacimiento, direccion, telefono)
        usuario_modelo.cerrar_conexion()
        return resultado

    @staticmethod
    def obtener_id_usuario(usuario):
        usuario_modelo = UsuarioModelo()
        usuario_id = usuario_modelo.obtener_id_usuario(usuario)
        usuario_modelo.cerrar_conexion()
        return usuario_id

    @staticmethod
    def obtener_usuario_por_id(usuario_id):
        usuario_modelo = UsuarioModelo()
        usuario = usuario_modelo.obtener_usuario_por_id(usuario_id)
        usuario_modelo.cerrar_conexion()
        return usuario

class ControladorDestino:
    def __init__(self):
        self.destino_modelo = DestinoModelo()

    def obtener_destinos(self):
        destinos = self.destino_modelo.obtener_destinos()
        # Retorna directamente las instancias de Destino
        return destinos

    def crear_destino(self, nombre, descripcion, actividades, costo):
        return self.destino_modelo.crear_destino(nombre, descripcion, actividades, costo)

    def actualizar_destino(self, id_destino, nombre, descripcion, actividades, costo):
        return self.destino_modelo.actualizar_destino(id_destino, nombre, descripcion, actividades, costo)

    def eliminar_destino(self, id_destino):
        self.destino_modelo.eliminar_paquete_destino_por_destino(id_destino)
        return self.destino_modelo.eliminar_destino(id_destino)

    def obtener_destino(self, id_destino):
        return self.destino_modelo.obtener_destino(id_destino)

    def cerrar_conexion(self):
        self.destino_modelo.cerrar_conexion()

class ControladorPaqueteTuristico:
    def __init__(self):
        self.paquete_modelo = PaqueteTuristicoModelo()
        self.destino_modelo = DestinoModelo()

    def obtener_paquetes_turisticos(self):
        return self.paquete_modelo.obtener_paquetes_turisticos()

    def crear_paquete_turistico(self, fecha_inicio, fecha_fin, destino_ids):
        destinos = self.destino_modelo.obtener_destinos_por_ids(destino_ids)
        if not destinos:
            return False
        precio_total = sum(destino['costo'] for destino in destinos)
        paquete_id = self.paquete_modelo.crear_paquete_turistico(fecha_inicio, fecha_fin, precio_total)
        print(paquete_id)
        input(2.2)
        if not paquete_id:
            return False
        for destino_id in destino_ids:
            if not self.paquete_modelo.agregar_destino_a_paquete(paquete_id, destino_id):
                return False
        return True

    def actualizar_paquete_turistico(self, id_paquete_turistico, fecha_inicio, fecha_fin, destino_ids):
        destinos = self.destino_modelo.obtener_destinos_por_ids(destino_ids)
        if not destinos:
            return False
        precio_total = sum(destino[4] for destino in destinos)
        if not self.paquete_modelo.actualizar_paquete_turistico(id_paquete_turistico, fecha_inicio, fecha_fin, precio_total):
            return False
        self.paquete_modelo.eliminar_destinos_de_paquete(id_paquete_turistico)
        for destino_id in destino_ids:
            if not self.paquete_modelo.agregar_destino_a_paquete(id_paquete_turistico, destino_id):
                return False
        return True

    def eliminar_paquete_turistico(self, id_paquete_turistico):
        resultado = self.paquete_modelo.eliminar_destinos_de_paquete(id_paquete_turistico)
        if resultado == False:
            return False
        return self.paquete_modelo.eliminar_paquete_turistico(id_paquete_turistico)

    def obtener_paquete_turistico(self, id_paquete_turistico):
        return self.paquete_modelo.obtener_paquete_turistico(id_paquete_turistico)

    def buscar_paquete_turistico_por_rango_fechas(self, fecha_inicio, fecha_fin):
        return self.paquete_modelo.buscar_paquete_turistico_por_rango_fechas(fecha_inicio, fecha_fin)

    def obtener_destinos_de_paquete(self, paquete_id):
        return self.paquete_modelo.obtener_destinos_de_paquete(paquete_id)

    def cerrar_conexion(self):
        self.paquete_modelo.cerrar_conexion()
        self.destino_modelo.cerrar_conexion()

class ControladorReserva:
    def __init__(self):
        self.reserva_modelo = ReservasModelo()

    def obtener_reservas(self):
        return self.reserva_modelo.obtener_reservas()

    def obtener_reserva(self, id_reserva):
        return self.reserva_modelo.obtener_reserva(id_reserva)

    def crear_reserva(self, usuario_id, paquete_id, fecha_reserva):
        return self.reserva_modelo.crear_reserva(usuario_id, paquete_id, fecha_reserva)

    def actualizar_reserva(self, id_reserva, usuario_id, paquete_id, fecha_reserva):
        return self.reserva_modelo.actualizar_reserva(id_reserva, usuario_id, paquete_id, fecha_reserva)

    def eliminar_reserva(self, id_reserva):
        return self.reserva_modelo.eliminar_reserva(id_reserva)

    def cancelar_reserva(self, id_reserva):
        return self.reserva_modelo.cancelar_reserva(id_reserva)

    def obtener_reservas_por_usuario(self, usuario_id):
        return self.reserva_modelo.obtener_reservas_por_usuario(usuario_id)

    def cerrar_conexion(self):
        self.reserva_modelo.cerrar_conexion()