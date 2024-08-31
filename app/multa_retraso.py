from calc_multa import EstrategiaCalculoMulta

class EstrategiaCalculoMultaPorRetraso(EstrategiaCalculoMulta):
    def calcular(self, prestamo):
        if prestamo.fechaDevolucion and prestamo.fechaDevolucion > prestamo.fechaDevolucionEstimada:
            dias_retraso = (prestamo.fechaDevolucion - prestamo.fechaDevolucionEstimada).days
            multa = dias_retraso * 2.0  # Ejemplo: $2 por día de retraso
            print(f"Multa calculada: ${multa}")
            return multa
        return 0.0