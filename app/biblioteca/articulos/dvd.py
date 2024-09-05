from articulos.articulo import Articulo

class DVD(Articulo):
    def __init__(self, id, titulo, autor, anio_publicacion, editorial, categoria, num_ejemplares, duracion, formato, genero):
        super().__init__(id, titulo, autor, anio_publicacion, editorial, categoria, num_ejemplares)
        self.duracion = duracion
        self.formato = formato
        self.genero = genero

    def detalles_dvd(self):
        return f"DVD: {self.titulo}, Duración: {self.duracion}, Género: {self.genero}"

    def reproducir_trailer(self):
        # Simula la reproducción de un tráiler
        print(f"Reproduciendo tráiler del DVD: {self.titulo}")
