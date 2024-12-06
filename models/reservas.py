# reservas_modelo.py
import mysql.connector
from .db_conn import DBConn


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

    def obtener_reservas_por_usuario(self, usuario_id):
        sql = """
        SELECT r.id, u.username, p.fecha_inicio, p.fecha_fin, r.fecha_reserva, r.paquete_id
        FROM Reservas r
        JOIN Usuarios u ON r.usuario_id = u.id
        JOIN PaquetesTuristicos p ON r.paquete_id = p.id
        WHERE r.usuario_id = %s
        """
        resultado = self.db.query(sql, (usuario_id,))
        return resultado

    def crear_reserva(self, usuario_id, paquete_id, fecha_reserva):
        try:
            sql = "INSERT INTO Reservas (usuario_id, paquete_id, fecha_reserva) VALUES (%s, %s, %s)"
            params = (usuario_id, paquete_id, fecha_reserva)
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def eliminar_reserva(self, id_reserva):
        try:
            sql = "DELETE FROM Reservas WHERE id = %s"
            params = (id_reserva,)
            self.db.execute(sql, params)
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def cerrar_conexion(self):
        self.db.cerrar_conexion()
