class Sugerencia:
    def __init__(self, id_sugerencia, usuario, mensaje):
        self.id_sugerencia = id_sugerencia
        self.usuario = usuario
        self.mensaje = mensaje
        self.fecha_envio = None

    def enviar_sugerencia(self):
        self.fecha_envio = "fecha_actual"  # Aquí usarías la fecha actual real
        print(f"Sugerencia enviada por {self.usuario.nombre_completo}: {self.mensaje}")

    def consultar_sugerencia(self):
        print(f"Sugerencia: {self.mensaje}, Fecha de Envío: {self.fecha_envio}")
