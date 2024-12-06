# Importa la clase ReservasModelo desde el módulo models.modelo
from models.reservas import ReservasModelo

# Define la clase ControladorReserva, que actúa como intermediario entre la vista y el modelo de datos
class ControladorReserva:
    def __init__(self):
        # Inicializa una instancia de ReservasModelo para manejar operaciones de reservas
        self.reserva_modelo = ReservasModelo()

    # Método para obtener todas las reservas
    def obtener_reservas(self):
        return self.reserva_modelo.obtener_reservas()

    # Método para obtener una reserva específica utilizando su ID
    def obtener_reserva(self, id_reserva):
        return self.reserva_modelo.obtener_reserva(id_reserva)

    # Método para crear una nueva reserva con los parámetros dados
    def crear_reserva(self, usuario_id, paquete_id, fecha_reserva):
        return self.reserva_modelo.crear_reserva(usuario_id, paquete_id, fecha_reserva)

    # Método para actualizar una reserva existente con los nuevos parámetros
    def actualizar_reserva(self, id_reserva, usuario_id, paquete_id, fecha_reserva):
        return self.reserva_modelo.actualizar_reserva(id_reserva, usuario_id, paquete_id, fecha_reserva)

    # Método para eliminar una reserva existente
    def eliminar_reserva(self, id_reserva):
        return self.reserva_modelo.eliminar_reserva(id_reserva)

    # Método para cancelar una reserva existente
    def cancelar_reserva(self, id_reserva):
        return self.reserva_modelo.cancelar_reserva(id_reserva)

    # Método para obtener todas las reservas de un usuario específico utilizando su ID
    def obtener_reservas_por_usuario(self, usuario_id):
        return self.reserva_modelo.obtener_reservas_por_usuario(usuario_id)

    # Método para cerrar la conexión a la base de datos
    def cerrar_conexion(self):
        self.reserva_modelo.cerrar_conexion()