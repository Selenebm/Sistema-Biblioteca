class Sujeto:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)
