# Clase Reserva - Para gestionar reservas de artículos
class Reserva:
    def __init__(self, ID, usuario, articulo, fechaReserva, estadoReserva="Activa"):
        self.ID = ID
        self.usuario = usuario
        self.articulo = articulo
        self.fechaReserva = fechaReserva
        self.estadoReserva = estadoReserva

    def cancelarReserva(self):
        self.estadoReserva = "Cancelada"
        print(f"Reserva de {self.articulo.titulo} cancelada.")

    def mostrarReserva(self):
        print(f"Reserva ID: {self.ID}, Usuario: {self.usuario.nombreCompleto}, Artículo: {self.articulo.titulo}, Fecha Reserva: {self.fechaReserva}, Estado: {self.estadoReserva}")
