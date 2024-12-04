import bcrypt
from baseDeDatos.db_conn import DBConn
import mysql.connector
import prettytable as pt


class UsuarioModelo:
    def __init__(self):
        self.db = DBConn()
        
=======
>>>>>>> 9d69efd1bd7a38d52b90220cf6d21234d01379f5:models/modelo.py


class Destino:
    def __init__(self, nombre, pais, descripcion):
        self.nombre = nombre
        self.pais = pais
        self.descripcion = descripcion

class DestinoModelo: 
    def __init__(self):
        self.db = DBConn()

    def obtener_destinos(self):
        try:
            sql = "SELECT * FROM Destinos"
            return self.db.query(sql)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def obtener_destino(self, id_destino):
        try:
            sql = "SELECT * FROM Destinos WHERE id = %s"
            params = (id_destino,)
            result = self.db.query(sql, params)
            return result[0] if result else None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def crear_destino(self, nombre, descripcion, actividades, costo):
        try:
            sql = "INSERT INTO Destinos (nombre, descripciones, actividades, costo) VALUES (%s, %s, %s, %s)"
            params = (nombre, descripcion, actividades, costo)
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
    
    def actualizar_destino(self, id_destino, nombre, descripcion, actividades, costo):
        try:
            sql = "UPDATE Destinos SET nombre = %s, descripciones = %s, actividades = %s, costo = %s WHERE id = %s"
            params = (nombre, descripcion, actividades, costo, id_destino)
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
    
    def eliminar_destino(self, id_destino):
        try:
            sql = "DELETE FROM Destinos WHERE id = %s"
            params = (id_destino,)
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def obtener_destinos_por_ids(self, destino_ids):
        try:
            format_strings = ','.join(['%s'] * len(destino_ids))
            sql = f"SELECT * FROM Destinos WHERE id IN ({format_strings})"
            params = tuple(destino_ids)
            return self.db.query(sql, params)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def eliminar_paquete_destino_por_destino(self, destino_id):
        try:
            sql = "DELETE FROM PaqueteDestino WHERE destino_id = %s"
            params = (destino_id,)
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def cerrar_conexion(self):
        self.db.cerrar_conexion()

class PaqueteTuristico:
    def __init__(self, paquete_destino):
        self.paquete_destino = paquete_destino

    def __str__(self):
        return f"Paquete Turistico con destinos: {[destino.nombre for destino in self.paquete_destino.destinos]}"

class PaqueteTuristicoModelo:
    def __init__(self):
        self.db = DBConn()

    def obtener_paquetes_turisticos(self):
        sql = """
        SELECT p.id, p.fecha_inicio, p.fecha_fin, p.precio_total, GROUP_CONCAT(d.nombre) AS destinos
        FROM PaquetesTuristicos p
        LEFT JOIN PaqueteDestino pd ON p.id = pd.paquete_id
        LEFT JOIN Destinos d ON pd.destino_id = d.id
        GROUP BY p.id
        """
        return self.db.query(sql)

    def obtener_paquete_turistico(self, id_paquete_turistico):
        sql = "SELECT id, fecha_inicio, fecha_fin, precio_total FROM PaquetesTuristicos WHERE id = %s"
        params = (id_paquete_turistico,)
        result = self.db.query(sql, params)
        return result[0] if result else None

    def crear_paquete_turistico(self, fecha_inicio, fecha_fin, precio_total):
        try:
            sql = "INSERT INTO PaquetesTuristicos (fecha_inicio, fecha_fin, precio_total) VALUES (%s, %s, %s)"
            params = (fecha_inicio, fecha_fin, precio_total)
            cursor = self.db.execute(sql, params)  # Now returns cursor
            return cursor.lastrowid  # Correctly access lastrowid
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def actualizar_paquete_turistico(self, id_paquete_turistico, fecha_inicio, fecha_fin, precio_total):
        sql = "UPDATE PaquetesTuristicos SET fecha_inicio = %s, fecha_fin = %s, precio_total = %s WHERE id = %s"
        params = (fecha_inicio, fecha_fin, precio_total, id_paquete_turistico)
        self.db.execute(sql, params)
        return True
    
    def buscar_paquete_turistico_por_rango_fechas(self, fecha_inicio, fecha_fin):
        sql = """
        SELECT p.id, p.fecha_inicio, p.fecha_fin, p.precio_total, GROUP_CONCAT(d.nombre) AS destinos, GROUP_CONCAT(d.actividades) AS actividades
        FROM PaquetesTuristicos p
        LEFT JOIN PaqueteDestino pd ON p.id = pd.paquete_id
        LEFT JOIN Destinos d ON pd.destino_id = d.id
        WHERE p.fecha_inicio >= %s AND p.fecha_fin <= %s
        GROUP BY p.id
        """
        params = (fecha_inicio, fecha_fin)
        return self.db.query(sql, params)

    def eliminar_paquete_turistico(self, id_paquete_turistico):
        sql = "DELETE FROM PaquetesTuristicos WHERE id = %s"
        params = (id_paquete_turistico,)
        self.db.execute(sql, params)
        return True

    def agregar_destino_a_paquete(self, paquete_id, destino_id):
        try:
            sql = "INSERT INTO PaqueteDestino (paquete_id, destino_id) VALUES (%s, %s)"
            params = (paquete_id, destino_id)
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def eliminar_destinos_de_paquete(self, paquete_id):
        try:
            sql = "SELECT paquete_id FROM PaqueteDestino WHERE paquete_id =%s"
            params = (paquete_id,)
            resultado = self.db.query(sql, params)
            if resultado == []:
                print("No existe el paquete turistico seleccionado...")
                return False
            sql = "DELETE FROM PaqueteDestino WHERE paquete_id = %s"
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def obtener_destinos_de_paquete(self, paquete_id):
        sql = """
        SELECT d.id, d.nombre, d.descripciones, d.actividades, d.costo
        FROM PaqueteDestino pd
        JOIN Destinos d ON pd.destino_id = d.id
        WHERE pd.paquete_id = %s
        """
        params = (paquete_id,)
        return self.db.query(sql, params)

    def cerrar_conexion(self):
        self.db.cerrar_conexion()

class Reserva:
    def __init__(self, usuario_id, paquete_id, fecha_reserva):
        self.usuario_id = usuario_id
        self.paquete_id = paquete_id
        self.fecha_reserva = fecha_reserva

class ReservasModelo:
    def __init__(self):
        self.db = DBConn()

    def obtener_reservas(self):
        sql = """
        SELECT r.id, u.username, p.fecha_inicio, p.fecha_fin, r.fecha_reserva
        FROM Reservas r
        JOIN Usuarios u ON r.usuario_id = u.id
        JOIN PaquetesTuristicos p ON r.paquete_id = p.id
        """
        return self.db.query(sql)

    def obtener_reserva(self, id_reserva):
        sql = "SELECT * FROM Reservas WHERE id = %s"
        params = (id_reserva,)
        return self.db.query(sql, params)

    def crear_reserva(self, usuario_id, paquete_id, fecha_reserva):
        sql = "INSERT INTO Reservas (usuario_id, paquete_id, fecha_reserva) VALUES (%s, %s, %s)"
        params = (usuario_id, paquete_id, fecha_reserva)
        self.db.execute(sql, params)
        return True
    
    def actualizar_reserva(self, id_reserva, usuario_id, paquete_id, fecha_reserva):
        sql = "UPDATE Reservas SET usuario_id = %s, paquete_id = %s, fecha_reserva = %s WHERE id = %s"
        params = (usuario_id, paquete_id, fecha_reserva, id_reserva)
        self.db.execute(sql, params)
        return True
    
    def eliminar_reserva(self, id_reserva):
        sql = "DELETE FROM Reservas WHERE id = %s"
        params = (id_reserva,)
        self.db.execute(sql, params)
        return True

    def obtener_reservas_por_usuario(self, usuario_id):
        sql = """
        SELECT r.id, r.usuario_id, r.paquete_id, r.fecha_reserva
        FROM Reservas r
        WHERE r.usuario_id = %s
        """
        params = (usuario_id,)
        return self.db.query(sql, params)

    def cerrar_conexion(self):
        self.db.cerrar_conexion()


class PaqueteDestino:
    def __init__(self):
        self.destinos = []

    def add_destino(self, destino):
        self.destinos.append(destino)

class PaqueteDestinoModelo:
    def __init__(self):
        self.db = DBConn()

    def agregar_paquete_destino(self, paquete_id, destino_id):
        try:
            sql = "INSERT INTO PaqueteDestino (paquete_id, destino_id) VALUES (%s, %s)"
            params = (paquete_id, destino_id)
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def obtener_paquetes_destino(self):
        try:
            sql = "SELECT * FROM PaqueteDestino"
            return self.db.query(sql)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def obtener_paquete_destino(self, paquete_id, destino_id):
        try:
            sql = """
            SELECT pd.paquete_id, pd.destino_id, p.fecha_inicio, p.fecha_fin, d.nombre, d.pais, d.descripcion
            FROM PaqueteDestino pd
            JOIN PaquetesTuristicos p ON pd.paquete_id = p.id
            JOIN Destinos d ON pd.destino_id = d.id
            WHERE pd.paquete_id = %s AND pd.destino_id = %s
            """
            params = (paquete_id, destino_id)
            return self.db.query(sql, params)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def actualizar_paquete_destino(self, paquete_id, destino_id, nuevo_paquete_id, nuevo_destino_id):
        try:
            sql = "UPDATE PaqueteDestino SET paquete_id = %s, destino_id = %s WHERE paquete_id = %s AND destino_id = %s"
            params = (nuevo_paquete_id, nuevo_destino_id, paquete_id, destino_id)
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def eliminar_paquete_destino(self, paquete_id, destino_id):
        try:
            sql = "DELETE FROM PaqueteDestino WHERE paquete_id = %s AND destino_id = %s"
            params = (paquete_id, destino_id)
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def cerrar_conexion(self):
        self.db.cerrar_conexion()




if __name__ == '__main__':
    """ # Search by date range and print results in a table
    modelo = PaqueteTuristicoModelo()
    paquetes = modelo.buscar_paquete_turistico_por_rango_fechas('2019-01-01', '2022-12-31')
    table = pt.PrettyTable()
    table.field_names = ["ID", "Fecha Inicio", "Fecha Fin", "Precio Total", "Destinos", "Actividades"]
    for paquete in paquetes:
        table.add_row(paquete)
    print(table)
    modelo.cerrar_conexion() """
    pass