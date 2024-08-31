from usuario import Usuario

class Bibliotecario(Usuario):
    def __init__(self, ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion):
        super().__init__(ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion)

    def registrarArticulo(self, catalogo, articulo):
        catalogo.agregarArticulo(articulo)

    def eliminarArticulo(self, catalogo, articulo):
        catalogo.eliminarArticulo(articulo)

    def gestionarMultas(self):
        print("Gestionando multas...")

    def generarReportes(self):
        print("Generando reportes...")