class Reporte:
    def __init__(self, id_reporte, tipo_reporte, datos):
        self.id_reporte = id_reporte
        self.tipo_reporte = tipo_reporte
        self.datos = datos

    def generar_reporte(self):
        print(f"Generando reporte de tipo: {self.tipo_reporte}")
        # Implementa lógica de generación de reporte en base a tipo y datos
