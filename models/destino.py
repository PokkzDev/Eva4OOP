# destino_modelo.py
import mysql.connector
from db_conn import DBConn


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
