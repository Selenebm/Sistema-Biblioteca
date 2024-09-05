from articulo import Articulo

class Libro(Articulo):
    def __init__(self, id, titulo, autor, anio_publicacion, editorial, isbn, categoria, num_ejemplares, num_paginas, genero, formato):
        super().__init__(id, titulo, autor, anio_publicacion, editorial, isbn, categoria, num_ejemplares)
        self.num_paginas = num_paginas
        self.genero = genero
        self.formato = formato

    def consultar_indice(self):
        return f"Índice del libro {self.titulo}"

    def detalles(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Páginas: {self.num_paginas}"
