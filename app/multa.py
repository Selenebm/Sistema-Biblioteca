#Clase Multa - Para gestionar multas
class Multa:
    def __init__(self, monto, fechaAplicacion):
        self.monto = monto
        self.fechaAplicacion = fechaAplicacion

    def mostrarMulta(self):
        print(f"Multa: {self.monto}, Fecha de Aplicación: {self.fechaAplicacion}")