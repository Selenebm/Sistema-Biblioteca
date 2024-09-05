from articulos.articulo import Articulo

class CD(Articulo):
    def __init__(self, id, titulo, autor, anio_publicacion, editorial, categoria, num_ejemplares, num_pistas, genero_musical):
        super().__init__(id, titulo, autor, anio_publicacion, editorial, categoria, num_ejemplares)
        self.num_pistas = num_pistas
        self.genero_musical = genero_musical

    def detalles_cd(self):
        return f"CD: {self.titulo}, Pistas: {self.num_pistas}, Género: {self.genero_musical}"

    def mostrar_lista_de_pistas(self):
        # Simula mostrar lista de pistas
        print(f"Mostrando pistas del CD: {self.titulo}")
