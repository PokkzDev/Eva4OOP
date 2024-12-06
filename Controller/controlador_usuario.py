# Separalo en archivos correspondientes de cada clase este archivo en archivos distintos.
from models.creacion_usuarios import AdministracionUsuarios

class ControladorAdmin:
    def __init__(self):
        self.Administracion = AdministracionUsuarios()

    def crear_usuario(self):
        return self.Administracion.create_user()