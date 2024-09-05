from abc import ABC, abstractmethod

class Articulo(ABC):
    def __init__(self, id, titulo, autor, anio_publicacion, editorial, isbn, categoria, num_ejemplares):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.editorial = editorial
        self.isbn = isbn
        self.categoria = categoria
        self.num_ejemplares = num_ejemplares

    def actualizar_datos_articulo(self, titulo, autor, anio, editorial, isbn, categoria, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio
        self.editorial = editorial
        self.isbn = isbn
        self.categoria = categoria
        self.num_ejemplares = ejemplares

    def consultar_disponibilidad(self):
        return self.num_ejemplares > 0

    @abstractmethod
    def detalles(self):
        pass
