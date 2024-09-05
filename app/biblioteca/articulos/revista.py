from articulos.articulo import Articulo

class Revista(Articulo):
    def __init__(self, id, titulo, autor, anio_publicacion, editorial, categoria, num_ejemplares, numero_edicion, mes_publicacion, tema_principal):
        super().__init__(id, titulo, autor, anio_publicacion, editorial, categoria, num_ejemplares)
        self.numero_edicion = numero_edicion
        self.mes_publicacion = mes_publicacion
        self.tema_principal = tema_principal

    def detalles_revista(self):
        return f"Revista: {self.titulo}, Edición: {self.numero_edicion}, Tema: {self.tema_principal}"

    def consulta_editorial(self):
        # Simula la consulta del contenido editorial
        print(f"Consultando editorial de la revista: {self.titulo}")
