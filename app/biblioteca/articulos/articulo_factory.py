from libro import Libro
from revista import Revista
# Importar otras subclases de Articulo aquí

class ArticuloFactory:
    @staticmethod
    def crear_articulo(tipo, **kwargs):
        if tipo == "libro":
            return Libro(**kwargs)
        elif tipo == "revista":
            return Revista(**kwargs)
        # Agregar más tipos si es necesario
        else:
            raise ValueError("Tipo de artículo no reconocido.")
