class Notificacion:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def enviar(self):
        print(f"Enviando notificación: {self.mensaje}")
