import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class DBConn:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        self.cursor = self.db.cursor()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()
    
    def execute(self, sql, params=None):
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        self.db.commit()
        return cursor
    
    def cerrar_conexion(self):
        self.db.close()

if __name__ == "__main__":
    try:
        conn = DBConn()
        print("Conexion exitosa")
        conn.cerrar_conexion()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
