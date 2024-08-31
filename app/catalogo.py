from articulo import Articulo
import json

# Singleton - Clase Catalogo
class Catalogo:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Catalogo, cls).__new__(cls)
            cls._instance.articulos = []
        return cls._instance

    def buscarArticulo(self, criterio):
        resultados = [articulo for articulo in self.articulos if criterio.lower() in articulo.titulo.lower()]
        if resultados:
            print(f"Artículos encontrados: {[articulo.titulo for articulo in resultados]}")
        else:
            print("No se encontraron artículos con ese criterio.")

    def agregarArticulo(self, articulo):
        self.articulos.append(articulo)
        print(f"Artículo {articulo.titulo} agregado al catálogo.")

    def eliminarArticulo(self, articulo):
        if articulo in self.articulos:
            self.articulos.remove(articulo)
            print(f"Artículo {articulo.titulo} eliminado del catálogo.")
        else:
            print(f"Artículo {articulo.titulo} no encontrado en el catálogo.")

    def guardarCatalogo(self, archivo):
        with open(archivo, 'w') as file:
            json.dump([articulo.to_dict() for articulo in self.articulos], file, indent=4)

    def cargarCatalogo(self, archivo):
        with open(archivo, 'r') as file:
            articulos_dict = json.load(file)
            self.articulos = [Articulo.from_dict(d) for d in articulos_dict]