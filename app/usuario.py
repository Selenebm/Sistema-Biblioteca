# Clases base para usuarios y sus variaciones
class Usuario:
    def __init__(self, ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion):
        self.ID = ID
        self.nombreCompleto = nombreCompleto
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fechaNacimiento = fechaNacimiento
        self.ocupacion = ocupacion

    def mostrarInformacion(self):
        print(f"ID: {self.ID}, Nombre: {self.nombreCompleto}, Email: {self.email}")