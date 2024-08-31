from usuario import Usuario

class UsuarioConMulta(Usuario):
    def __init__(self, ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion, multaPendiente):
        super().__init__(ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion)
        self.multaPendiente = multaPendiente

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Multa pendiente: {self.multaPendiente}")