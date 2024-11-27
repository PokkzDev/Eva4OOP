import mysql.connector

class DBConn:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Asdf1234",
            database="viajes_aventura"
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
