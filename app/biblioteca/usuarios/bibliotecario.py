from usuario import Usuario

class Bibliotecario(Usuario):
    def gestionar_prestamo(self):
        print("Prestamo gestionado por bibliotecario.")

    def gestionar_devolucion(self):
        print("Devolución gestionada por bibliotecario.")

    def calcular_multa(self):
        print("Multa calculada.")
