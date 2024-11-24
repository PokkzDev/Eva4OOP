import sqlite3

def initialize_db():
    conn = sqlite3.connect('./baseDeDatos/viajes_aventura.db')
    cursor = conn.cursor()

    # Crear tabla de Destinos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Destinos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripciones TEXT,
            actividades TEXT,
            costo REAL NOT NULL
        )
    ''')

    # Crear tabla de Paquetes Turísticos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PaquetesTuristicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            destino_id INTEGER NOT NULL,
            fecha_inicio TEXT NOT NULL,
            fecha_fin TEXT NOT NULL,
            precio_total REAL NOT NULL,
            FOREIGN KEY (destino_id) REFERENCES Destinos(id)
        )
    ''')

    # Crear tabla de Usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            contrasena TEXT NOT NULL,
            rol TEXT CHECK(rol IN ('admin', 'cliente')) NOT NULL
        )
    ''')

    # Crear tabla de Reservas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            paquete_id INTEGER NOT NULL,
            fecha_reserva TEXT NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES Usuarios(id),
            FOREIGN KEY (paquete_id) REFERENCES PaquetesTuristicos(id)
        )
    ''')

if __name__ == '__main__':
    initialize_db()