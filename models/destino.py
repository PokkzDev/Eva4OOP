# destino_modelo.py
import mysql.connector
from .db_conn import DBConn


class Destino:
    def __init__(self, id, nombre, descripcion, actividades=None, costo=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.actividades = actividades
        self.costo = costo
    
    def __str__(self):
        return f"Destino(id={self.id}, nombre={self.nombre}, descripcion={self.descripcion}, actividades={self.actividades}, costo={self.costo})"


class DestinoModelo: 
    def __init__(self):
        self.db = DBConn()

    def obtener_destinos(self):
        try:
            sql = "SELECT id, nombre, descripciones, actividades, costo FROM Destinos"
            resultados = self.db.query(sql)
            destinos = []
            for row in resultados:
                # Asumiendo que 'row' es un diccionario con las claves 'id', 'nombre', 'descripcion', etc.
                destino = Destino(
                    id=row['id'],  # Usar las claves correspondientes
                    nombre=row['nombre'],
                    descripcion=row['descripciones'],  # Si es un diccionario
                )
                destino.actividades = row['actividades']
                destino.costo = row['costo']
                destinos.append(destino)
            return destinos
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
