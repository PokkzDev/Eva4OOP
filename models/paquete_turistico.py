# paquete_turistico_modelo.py
import mysql.connector
from .db_conn import DBConn


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
        resultado = self.db.query(sql)
        return resultado

    def obtener_paquete_turistico(self, id_paquete_turistico):
        sql = "SELECT id, fecha_inicio, fecha_fin, precio_total FROM PaquetesTuristicos WHERE id = %s"
        params = (id_paquete_turistico,)
        result = self.db.query(sql, params)
        return result[0] if result else None

    def crear_paquete_turistico(self, fecha_inicio, fecha_fin, precio_total):
        try:
            # Ejecuta la consulta para insertar un nuevo paquete turístico
            sql = "INSERT INTO PaquetesTuristicos (fecha_inicio, fecha_fin, precio_total) VALUES (%s, %s, %s)"
            params = (fecha_inicio, fecha_fin, precio_total)
            
            # Ejecuta la inserción, pero no necesitas el lastrowid
            resultado =self.db.execute_id(sql, params)
            return resultado  # Indica que la inserción fue exitosa
        except mysql.connector.Error as err:
            print(f"Error al crear paquete turístico: {err}")
            return False

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
