class Usuario:
    def __init__(self, id, nombre_completo, direccion, telefono, email, fecha_nacimiento, ocupacion):
        self.id = id
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.ocupacion = ocupacion

    def validar_identificacion(self):
        # Lógica para validar el ID del usuario
        return True

    def registrar_usuario(self):
        print(f"Usuario {self.nombre_completo} registrado con éxito.")

    def actualizar_datos(self, direccion, telefono, email):
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
