from usuarios.usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, id, nombre_completo, direccion, telefono, email, fecha_nacimiento, ocupacion, centro_estudios):
        super().__init__(id, nombre_completo, direccion, telefono, email, fecha_nacimiento, ocupacion)
        self.centro_estudios = centro_estudios

    def consultar_centro_estudios(self):
        print(f"Centro de Estudios: {self.centro_estudios}")
