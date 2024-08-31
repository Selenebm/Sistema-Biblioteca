# Clase Prestamo - Para gestionar préstamos
class Prestamo:
    def __init__(self, ID, usuario, articulo, fechaPrestamo, fechaDevolucionEstimada, estrategia_calculo_multa=None):
        self.ID = ID
        self.usuario = usuario
        self.articulo = articulo
        self.fechaPrestamo = fechaPrestamo
        self.fechaDevolucionEstimada = fechaDevolucionEstimada
        self.fechaDevolucion = None
        self.estrategia_calculo_multa = estrategia_calculo_multa

    def devolver(self, fechaDevolucion):
        self.fechaDevolucion = fechaDevolucion
        print(f"Artículo {self.articulo.titulo} devuelto por {self.usuario.nombreCompleto} el {self.fechaDevolucion}")
        self.calcularMulta()

    def calcularMulta(self):
        if self.estrategia_calculo_multa:
            return self.estrategia_calculo_multa.calcular(self)
        return 0.0

    def calcularRenovacion(self):
        print(f"Préstamo de {self.articulo.titulo} renovado.")