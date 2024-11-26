import re
from modelo import UsuarioModelo

class Controlador:
    def __init__(self, modelo):
        self.modelo = modelo

    def iniciar_sesion(self, usuario, contrasena):
        
        return self.modelo.verificar_usuario(usuario, contrasena)

    def registrarse(self, username, password, confirm_password):
        validations = [
            (not username, "El nombre de usuario no puede estar vacío."),
            (len(username) < 5, "El nombre de usuario debe tener al menos 5 caracteres."),
            (password != confirm_password, "Las contraseñas no coinciden."),
            (not password, "La contraseña no puede estar vacía."),
            (len(password) < 8, "La contraseña debe tener al menos 8 caracteres."),
            (not re.search(r"[A-Z]", password), "La contraseña debe contener al menos una letra mayúscula."),
            (not re.search(r"[a-z]", password), "La contraseña debe contener al menos una letra minúscula."),
            (not re.search(r"[0-9]", password), "La contraseña debe contener al menos un número."),
            (not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password), "La contraseña debe contener al menos un carácter especial.")
        ]

        for condition, message in validations:
            if condition:
                return False, message

        if self.modelo.registrar_usuario(username, password):
            return True, "Registro exitoso."
        else:
            return False, "El usuario ya existe. Intente con otro nombre de usuario."

# Example usage
# controlador = Controlador(modelo)
