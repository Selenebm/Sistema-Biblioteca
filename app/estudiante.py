from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion, centroEstudios):
        super().__init__(ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion)
        self.centroEstudios = centroEstudios

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Centro de Estudios: {self.centroEstudios}")
