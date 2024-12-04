# usuario_modelo.py
import bcrypt
import mysql.connector
from baseDeDatos.db_conn import DBConn

class Usuario:
    def __init__(self, id=None, username=None, password=None, rol=None, hasDatosPersonales=False):
        self.id = id
        self.username = username
        self.__password = password  # Atributo privado
        self.__rol = rol  # Atributo privado
        self.__hasDatosPersonales = hasDatosPersonales  # Atributo privado

    def verificar_usuario(self, username, contrasena):
        """
        Verifica si el nombre de usuario y la contraseña proporcionados coinciden
        con los almacenados en el objeto.
        """
        return (
            username == self.username and
            bcrypt.checkpw(contrasena.encode('utf-8'), self.__password.encode('utf-8'))
        )

    def get_rol(self):
        """Retorna el rol del usuario."""
        return self.__rol

    def __str__(self):
        return f"Usuario(id={self.id}, username={self.username}, rol={self.__rol}, hasDatosPersonales={self.__hasDatosPersonales})"

# usuario_modelo.py
class UsuarioDatosPersonales:
    def __init__(self, usuario_id, nombre, apellido, fecha_nacimiento, direccion, telefono):
        self.__usuario_id = usuario_id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        self.__direccion = direccion
        self.__telefono = telefono

    # Getters (Métodos para acceder a los atributos)
    def get_usuario_id(self):
        return self.__usuario_id

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono

    # Setters (Métodos para modificar los atributos)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def __str__(self):
        return f"UsuarioDatosPersonales(usuario_id={self.__usuario_id}, nombre={self.__nombre}, apellido={self.__apellido}, fecha_nacimiento={self.__fecha_nacimiento}, direccion={self.__direccion}, telefono={self.__telefono})"


class UsuarioModelo:
    def __init__(self):
        self.db = DBConn()

    def verificar_usuario(self, username, contrasena):
        """Verifica si el username existe y si la contraseña es correcta."""
        try:
            sql = "SELECT * FROM Usuarios WHERE username = %s"
            params = (username,)
            result = self.db.query(sql, params)
            if not result:
                return None
            
            user_data = result[0]
            user = Usuario(id=user_data[0], username=user_data[1], password=user_data[2], rol=user_data[3], hasDatosPersonales=user_data[4],)
            return user if user.verificar_usuario(username, contrasena) else None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def registrar_usuario(self, usuario, contrasena):
        """Registra un nuevo usuario, creando una contraseña hasheada."""
        try:
            sql = "SELECT * FROM Usuarios WHERE username = %s"
            params = (usuario,)
            if self.db.query(sql, params):
                return False
            hashed = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            sql = "INSERT INTO Usuarios (username, password, rol) VALUES (%s, %s, %s)"
            params = (usuario, hashed, 'cliente')  # O 'admin' si es el primer usuario
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
    
    def agregar_datos_personales(self, usuario_id, nombre, apellido, fecha_nacimiento, direccion, telefono):
        try:
            # Creación de un objeto UsuarioDatosPersonales
            datos_personales = UsuarioDatosPersonales(usuario_id, nombre, apellido, fecha_nacimiento, direccion, telefono)
            
            # Inserción de datos personales en la base de datos
            sql = "INSERT INTO usuario_datos_personales (usuario_id, nombre, apellido, fecha_nacimiento, direccion, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
            params = (datos_personales.get_usuario_id(), datos_personales.get_nombre(), datos_personales.get_apellido(),
                    datos_personales.get_fecha_nacimiento(), datos_personales.get_direccion(), datos_personales.get_telefono())
            self.db.execute(sql, params)

            # Cambiar el flag hasDatosPersonales en la tabla Usuarios
            sql = "UPDATE Usuarios SET hasDatosPersonales = 1 WHERE id = %s"
            params = (usuario_id,)
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False


    def obtener_id_usuario(self, usuario):
        """Obtiene el id de un usuario por su username."""
        try:
            sql = "SELECT id FROM Usuarios WHERE username = %s"
            params = (usuario,)
            result = self.db.query(sql, params)
            return result[0][0] if result else None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def obtener_usuario_por_id(self, usuario_id):
        """Obtiene los datos de un usuario por su id."""
        try:
            sql = "SELECT * FROM Usuarios WHERE id = %s"
            params = (usuario_id,)
            result = self.db.query(sql, params)
            if result:
                user_data = result[0]
                return Usuario(id=user_data[0], username=user_data[1], password=user_data[2], rol=user_data[3], hasDatosPersonales=user_data[4])
            return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos."""
        self.db.cerrar_conexion()
