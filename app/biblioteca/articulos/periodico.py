from articulos.articulo import Articulo

class Periodico(Articulo):
    def __init__(self, id, titulo, autor, anio_publicacion, editorial, categoria, num_ejemplares, fecha_publicacion, num_edicion, tema_principal):
        super().__init__(id, titulo, autor, anio_publicacion, editorial, categoria, num_ejemplares)
        self.fecha_publicacion = fecha_publicacion
        self.num_edicion = num_edicion
        self.tema_principal = tema_principal

    def detalles_periodico(self):
        return f"Periódico: {self.titulo}, Fecha: {self.fecha_publicacion}, Tema: {self.tema_principal}"

    def consulta_portada(self):
        # Simula la consulta de la portada
        print(f"Mostrando portada del Periódico: {self.titulo}")
