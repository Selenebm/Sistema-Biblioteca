class Prestamo:
    def __init__(self, id_prestamo, usuario, articulo, fecha_prestamo, fecha_devolucion_estimada, tipo_prestamo):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.articulo = articulo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion_estimada = fecha_devolucion_estimada
        self.multa = 0
        self.tipo_prestamo = tipo_prestamo

    def registrar_prestamo(self):
        print(f"Préstamo registrado: {self.articulo.titulo} para {self.usuario.nombre_completo}")

    def actualizar_devolucion(self):
        print(f"Devolución del artículo {self.articulo.titulo} actualizada.")

    def calcular_multa(self):
        # Lógica para calcular multa por retraso
        print(f"Multa calculada: {self.multa}")
