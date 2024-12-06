# Importa la clase DestinoModelo desde el módulo models.modelo
from models.modelo import DestinoModelo

# Define la clase ControladorDestino, que actúa como intermediario entre la vista y el modelo de datos
class ControladorDestino:
    def __init__(self):
        # Inicializa una instancia de DestinoModelo
        self.destino_modelo = DestinoModelo()

    # Método para obtener todos los destinos
    def obtener_destinos(self):
        return self.destino_modelo.obtener_destinos()
    
    # Método para crear un nuevo destino
    def crear_destino(self, nombre, descripcion, actividades, costo):
        return self.destino_modelo.crear_destino(nombre, descripcion, actividades, costo)
    
    # Método para actualizar un destino existente
    def actualizar_destino(self, id_destino, nombre, descripcion, actividades, costo):
        return self.destino_modelo.actualizar_destino(id_destino, nombre, descripcion, actividades, costo)

    # Método para eliminar un destino
    def eliminar_destino(self, id_destino):
        self.destino_modelo.eliminar_paquete_destino_por_destino(id_destino)
        return self.destino_modelo.eliminar_destino(id_destino)

    # Método para obtener los detalles de un destino específico usando su ID
    def obtener_destino(self, id_destino):
        return self.destino_modelo.obtener_destino(id_destino)
    
    # Método para cerrar la conexión a la base de datos
    def cerrar_conexion(self):
        self.destino_modelo.cerrar_conexion()
