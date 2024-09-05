class Reserva:
    def __init__(self, id_reserva, usuario, articulo, fecha_reserva):
        self.id_reserva = id_reserva
        self.usuario = usuario
        self.articulo = articulo
        self.fecha_reserva = fecha_reserva
        self.estado_reserva = "Pendiente"

    def registrar_reserva(self):
        print(f"Reserva registrada para el artículo '{self.articulo.titulo}' por el usuario {self.usuario.nombre_completo}")

    def actualizar_estado_reserva(self, nuevo_estado):
        self.estado_reserva = nuevo_estado
        print(f"Estado de la reserva actualizado a: {self.estado_reserva}")
