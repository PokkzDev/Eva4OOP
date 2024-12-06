# Separalo en archivos correspondientes de cada clase este archivo en archivos distintos.

from models.modelo import UsuarioModelo
from models.modelo import DestinoModelo
from models.modelo import PaqueteTuristicoModelo
from models.modelo import ReservasModelo

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