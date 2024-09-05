class Observador:
    def actualizar(self, mensaje):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")


class UsuarioObservador(Observador):
    def __init__(self, usuario):
        self.usuario = usuario

    def actualizar(self, mensaje):
        print(f"Notificación para {self.usuario.nombre_completo}: {mensaje}")

