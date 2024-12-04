# db_conn.py
import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error

load_dotenv()

class DBConn:
    def __init__(self):
        self.connection = self.conectar()

    def conectar(self):
        try:
            connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
            return connection
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def query(self, sql, params=None):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(sql, params or ())
        return cursor.fetchall()

    def execute(self, sql, params=None):
        cursor = self.connection.cursor()
        cursor.execute(sql, params or ())
        self.connection.commit()

    def cerrar_conexion(self):
        if self.connection:
            self.connection.close()
