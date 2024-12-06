# Importa las clases DestinoModelo y PaqueteTuristicoModelo desde el módulo models.modelo
from models.destino import DestinoModelo
from models.paquete_turistico import PaqueteTuristicoModelo


# Define la clase ControladorPaqueteTuristico, que actúa como intermediario entre la vista y el modelo de datos
class ControladorPaqueteTuristico:
    def __init__(self):
        # Inicializa una instancia de PaqueteTuristicoModelo para manejar operaciones de paquetes turísticos
        self.paquete_modelo = PaqueteTuristicoModelo()
        # Inicializa una instancia de DestinoModelo para manejar operaciones relacionadas con destinos
        self.destino_modelo = DestinoModelo()

    # Método para obtener todos los paquetes turísticos
    def obtener_paquetes_turisticos(self):
        return self.paquete_modelo.obtener_paquetes_turisticos()

    # Método para crear un nuevo paquete turístico con los parámetros dados
    def crear_paquete_turistico(self, fecha_inicio, fecha_fin, destino_ids):
        # Obtiene los destinos utilizando los IDs proporcionados
        destinos = self.destino_modelo.obtener_destinos_por_ids(destino_ids)
        if not destinos:
            return False
        
        # Calcula el precio total sumando los costos de los destinos
        precio_total = sum(destino[4] for destino in destinos) 

        # Crea un nuevo paquete turístico con la fecha de inicio, fecha de fin y el precio total 
        paquete_id = self.paquete_modelo.crear_paquete_turistico(fecha_inicio, fecha_fin, precio_total)
        if not paquete_id:
            return False
        
        # Agrega cada destino al paquete turístico creado
        for destino_id in destino_ids:
            if not self.paquete_modelo.agregar_destino_a_paquete(paquete_id, destino_id):
                return False
        return True
    
    # Método para actualizar un paquete turístico existente con los nuevos parámetros
    def actualizar_paquete_turistico(self, id_paquete_turistico, fecha_inicio, fecha_fin, destino_ids):
        # Obtiene los destinos utilizando los IDs proporcionados
        destinos = self.destino_modelo.obtener_destinos_por_ids(destino_ids)
        if not destinos:
            return False
        
        # Calcula el precio total sumando los costos de los destinos
        precio_total = sum(destino[4] for destino in destinos)

        # Actualiza el paquete turístico con la nueva información
        if not self.paquete_modelo.actualizar_paquete_turistico(id_paquete_turistico, fecha_inicio, fecha_fin, precio_total):
            return False
        
        # Elimina los destinos actuales del paquete
        self.paquete_modelo.eliminar_destinos_de_paquete(id_paquete_turistico)

        # Agrega cada nuevo destino al paquete actualizado
        for destino_id in destino_ids:
            if not self.paquete_modelo.agregar_destino_a_paquete(id_paquete_turistico, destino_id):
                return False
        return True

    # Método para eliminar un paquete turístico existente
    def eliminar_paquete_turistico(self, id_paquete_turistico):
        # Elimina los destinos asociados al paquete turístico
        resultado = self.paquete_modelo.eliminar_destinos_de_paquete(id_paquete_turistico)
        if resultado == False:
            return False
        
        # Elimina el paquete turístico en sí
        return self.paquete_modelo.eliminar_paquete_turistico(id_paquete_turistico)

    # Método para obtener los detalles de un paquete turístico específico utilizando su ID
    def obtener_paquete_turistico(self, id_paquete_turistico):
        return self.paquete_modelo.obtener_paquete_turistico(id_paquete_turistico)

    # Método para buscar paquetes turísticos dentro de un rango de fechas
    def buscar_paquete_turistico_por_rango_fechas(self, fecha_inicio, fecha_fin):
        return self.paquete_modelo.buscar_paquete_turistico_por_rango_fechas(fecha_inicio, fecha_fin)

    # Método para obtener los destinos asociados a un paquete turístico específico
    def obtener_destinos_de_paquete(self, paquete_id):
        return self.paquete_modelo.obtener_destinos_de_paquete(paquete_id)

    # Método para cerrar la conexión a la base de datos
    def cerrar_conexion(self):
        self.paquete_modelo.cerrar_conexion()
        self.destino_modelo.cerrar_conexion()
