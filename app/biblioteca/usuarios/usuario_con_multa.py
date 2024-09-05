from usuarios.usuario import Usuario

class UsuarioConMulta(Usuario):
    def __init__(self, id, nombre_completo, direccion, telefono, email, fecha_nacimiento, ocupacion, multa_pendiente=0.0):
        super().__init__(id, nombre_completo, direccion, telefono, email, fecha_nacimiento, ocupacion)
        self.multa_pendiente = multa_pendiente

    def verificar_multa(self):
        print(f"Multa pendiente: {self.multa_pendiente}")
        return self.multa_pendiente > 0

    def bloquear_prestamo(self):
        if self.verificar_multa():
            print(f"El usuario {self.nombre_completo} tiene multas pendientes y no puede realizar préstamos.")
        else:
            print(f"El usuario {self.nombre_completo} no tiene multas pendientes.")
