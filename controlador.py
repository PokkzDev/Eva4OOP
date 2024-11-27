# RE TAL VEZ PARA VALIDACIONES DE CAMPOS DE TEXTO
import re
from modelo import UsuarioModelo
from modelo import DestinoModelo
from modelo import PaqueteTuristicoModelo

class Controlador:
    @staticmethod
    def iniciar_sesion(usuario, contrasena):
        usuario_modelo = UsuarioModelo()
        resultado = usuario_modelo.verificar_usuario(usuario, contrasena)
        usuario_modelo.cerrar_conexion()
        return resultado

    @staticmethod
    def registrarse(usuario, contrasena):
        # TODO: Implementar lógica para registrar un nuevo usuario
        
        pass

    @staticmethod
    def agregar_datos_personales(usuario, nombre, apellido, correo, telefono):
        # TODO: nombre, apellido, fecha_nacimiento, direccion, telefono, correo
        pass

class ControladorDestino:
    def __init__(self):
        self.destino_modelo = DestinoModelo()

    def obtener_destinos(self):
        return self.destino_modelo.obtener_destinos()

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
        precio_total = sum(destino[4] for destino in destinos)  
        paquete_id = self.paquete_modelo.crear_paquete_turistico(fecha_inicio, fecha_fin, precio_total)
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
        self.paquete_modelo.eliminar_destinos_de_paquete(id_paquete_turistico)
        return self.paquete_modelo.eliminar_paquete_turistico(id_paquete_turistico)

    def obtener_paquete_turistico(self, id_paquete_turistico):
        return self.paquete_modelo.obtener_paquete_turistico(id_paquete_turistico)

    def cerrar_conexion(self):
        self.paquete_modelo.cerrar_conexion()
        self.destino_modelo.cerrar_conexion()