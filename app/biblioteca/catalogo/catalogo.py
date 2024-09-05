class Catalogo:
    def __init__(self):
        self.articulos = []

    def agregar_articulo(self, articulo):
        self.articulos.append(articulo)
        print(f"Artículo '{articulo.titulo}' agregado al catálogo.")

    def eliminar_articulo(self, id_articulo):
        self.articulos = [art for art in self.articulos if art.id != id_articulo]
        print(f"Artículo con ID '{id_articulo}' eliminado del catálogo.")

    def buscar_articulo(self, id_articulo):
        for art in self.articulos:
            if art.id == id_articulo:
                return art
        return None

    def listar_articulos(self):
        return self.articulos
