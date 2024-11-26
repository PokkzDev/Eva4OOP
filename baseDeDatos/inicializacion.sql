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
    FOREIGN KEY (paquete_id) REFERENCES PaquetesTuristicos(id),
    FOREIGN KEY (destino_id) REFERENCES Destinos(id)
);

-- Crear tabla de Usuarios
CREATE TABLE IF NOT EXISTS Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'cliente') NOT NULL
);

-- Crear tabla de Reservas
CREATE TABLE IF NOT EXISTS Reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    paquete_id INT NOT NULL,
    fecha_reserva DATE NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id),
    FOREIGN KEY (paquete_id) REFERENCES PaquetesTuristicos(id)
);