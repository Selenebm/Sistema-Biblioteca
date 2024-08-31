from abc import ABC, abstractmethod

# Strategy - Clases para definir diferentes estrategias de cálculo de multas
class EstrategiaCalculoMulta(ABC):
    @abstractmethod
    def calcular(self, prestamo):
        pass