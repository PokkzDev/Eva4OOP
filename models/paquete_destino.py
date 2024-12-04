# paquete_destino_modelo.py
import mysql.connector
from db_conn import DBConn


class PaqueteDestinoModelo:
    def __init__(self):
        self.db = DBConn()

    def eliminar_destino_de_paquete(self, paquete_id, destino_id):
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
