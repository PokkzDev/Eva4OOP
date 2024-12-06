# Importa la clase UsuarioModelo desde el módulo models.modelo
from models.modelo import UsuarioModelo

# Define la clase Controlador, que maneja las operaciones relacionadas con usuarios
class Controlador:
    @staticmethod
    def iniciar_sesion(usuario, contrasena):

        # Crea una instancia de UsuarioModelo para interactuar con la base de datos
        usuario_modelo = UsuarioModelo()

        # Verifica las credenciales del usuario
        resultado = usuario_modelo.verificar_usuario(usuario, contrasena)

        # Cierra la conexión a la base de datos
        usuario_modelo.cerrar_conexion()

        # Retorna el resultado de la verificación
        return resultado

    @staticmethod
    def registrarse(usuario, contrasena):

        # Crea una instancia de UsuarioModelo para interactuar con la base de datos
        usuario_modelo = UsuarioModelo()

        # Intenta registrar un nuevo usuario
        resultado = usuario_modelo.registrar_usuario(usuario, contrasena)

        # Imprime un mensaje si el nombre de usuario ya existe
        if resultado == False:
            print("Ya existe ese nombre de usuario")

        # Cierra la conexión a la base de datos
        usuario_modelo.cerrar_conexion()

        # Retorna el resultado del registro
        return resultado

    @staticmethod
    def agregar_datos_personales(usuario_id, nombre, apellido, fecha_nacimiento, direccion, telefono):

        # Crea una instancia de UsuarioModelo para interactuar con la base de datos
        usuario_modelo = UsuarioModelo()

        # Agrega datos personales para el usuario especificado
        resultado = usuario_modelo.agregar_datos_personales(usuario_id, nombre, apellido, fecha_nacimiento, direccion, telefono)

        # Cierra la conexión a la base de datos
        usuario_modelo.cerrar_conexion()

        # Retorna el resultado de la operación
        return resultado

    @staticmethod
    def obtener_id_usuario(usuario):

        # Crea una instancia de UsuarioModelo para interactuar con la base de datos
        usuario_modelo = UsuarioModelo()

        # Obtiene el ID del usuario basado en el nombre de usuario
        usuario_id = usuario_modelo.obtener_id_usuario(usuario)

        # Cierra la conexión a la base de datos
        usuario_modelo.cerrar_conexion()

        # Retorna el ID del usuario
        return usuario_id

    @staticmethod
    def obtener_usuario_por_id(usuario_id):

        # Crea una instancia de UsuarioModelo para interactuar con la base de datos
        usuario_modelo = UsuarioModelo()

        # Obtiene los detalles del usuario basado en su ID
        usuario = usuario_modelo.obtener_usuario_por_id(usuario_id)

        # Cierra la conexión a la base de datos
        usuario_modelo.cerrar_conexion()

        # Retorna los detalles del usuario
        return usuario