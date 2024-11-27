-- Eliminar base de datos si existe
DROP DATABASE IF EXISTS viajes_aventura;

-- Crear base de datos si no existe
CREATE DATABASE IF NOT EXISTS viajes_aventura;
USE viajes_aventura;

-- Crear tabla de Destinos
CREATE TABLE IF NOT EXISTS Destinos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL UNIQUE,
    descripciones TEXT,
    actividades TEXT,
    costo FLOAT NOT NULL
);

-- Crear tabla de Paquetes Turísticos
CREATE TABLE IF NOT EXISTS PaquetesTuristicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    precio_total FLOAT NOT NULL
);

-- Crear tabla de relación entre Paquetes Turísticos y Destinos
CREATE TABLE IF NOT EXISTS PaqueteDestino (
    paquete_id INT NOT NULL,
    destino_id INT NOT NULL,
    PRIMARY KEY (paquete_id, destino_id),
    FOREIGN KEY (paquete_id) REFERENCES PaquetesTuristicos(id) ON DELETE CASCADE,
    FOREIGN KEY (destino_id) REFERENCES Destinos(id) ON DELETE CASCADE
);

-- Crear tabla de Usuarios
CREATE TABLE IF NOT EXISTS Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    hasDatosPersonales BOOLEAN DEFAULT FALSE,
    rol ENUM('admin', 'cliente') NOT NULL
    
);

-- Crear tabla de Datos Personales de Usuarios
CREATE TABLE IF NOT EXISTS usuario_datos_personales (
    usuario_id INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE,
    direccion TEXT,
    telefono VARCHAR(50),
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id) ON DELETE CASCADE
);

-- Crear tabla de Reservas
CREATE TABLE IF NOT EXISTS Reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    paquete_id INT NOT NULL,
    fecha_reserva DATE NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (paquete_id) REFERENCES PaquetesTuristicos(id) ON DELETE CASCADE
);

-- Insert mock data for Destinos
INSERT INTO Destinos (nombre, descripciones, actividades, costo) VALUES
('Playa Paraíso', 'Hermosa playa con aguas cristalinas.', 'Nado, snorkel, relax', 1200.0),
('Montaña Mística', 'Montañas llenas de misterio y naturaleza.', 'Senderismo, escalada', 1500.0),
('Ciudad Historia', 'Ciudad rica en historia y cultura.', 'Visitas guiadas, museos', 1000.0),
('Isla Tropical', 'Isla exótica con fauna diversa.', 'Buceo, pesca, exploración', 1800.0),
('Desierto Dorado', 'Extensos desiertos con paisajes únicos.', 'Tours en camello, fotografía', 1300.0);

-- Insert mock data for Paquetes Turísticos
INSERT INTO PaquetesTuristicos (fecha_inicio, fecha_fin, precio_total) VALUES
('2024-06-01', '2024-06-10', 5000.0),
('2024-07-15', '2024-07-25', 7500.0);

-- Insert mock data for PaqueteDestino
INSERT INTO PaqueteDestino (paquete_id, destino_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(2, 5);

DELIMITER //

DROP TRIGGER IF EXISTS actualizar_precio_paquete //

CREATE TRIGGER actualizar_precio_paquete
AFTER UPDATE ON Destinos
FOR EACH ROW
BEGIN
    UPDATE PaquetesTuristicos pt
    SET precio_total = (
        SELECT IFNULL(SUM(d.costo), 0)
        FROM PaqueteDestino pd
        JOIN Destinos d ON pd.destino_id = d.id
        WHERE pd.paquete_id = pt.id
    )
    WHERE pt.id IN (
        SELECT pd.paquete_id
        FROM PaqueteDestino pd
        WHERE pd.destino_id = NEW.id
    );
END //

DELIMITER ;