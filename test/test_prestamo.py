import unittest
from prestamos.prestamo import Prestamo
from usuarios.usuario import Usuario
from articulos.libro import Libro

class TestPrestamo(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario(
            id="u123",
            nombre_completo="Juan Pérez",
            direccion="Calle Falsa 123",
            telefono="555-1234",
            email="juan@example.com",
            fecha_nacimiento="1990-01-01",
            ocupacion="Estudiante"
        )
        self.libro = Libro(
            id="123",
            titulo="Cien años de soledad",
            autor="Gabriel García Márquez",
            anio_publicacion=1967,
            editorial="Editorial Sudamericana",
            isbn="978-3-16-148410-0",
            categoria="Novela",
            num_ejemplares=10,
            num_paginas=471,
            genero="Ficción",
            formato="Tapa dura"
        )
        self.prestamo = Prestamo(
            id_prestamo="p123",
            usuario=self.usuario,
            articulo=self.libro,
            fecha_prestamo="2024-09-01",
            fecha_devolucion_estimada="2024-09-10",
            tipo_prestamo="Largo plazo"
        )

    def test_registrar_prestamo(self):
        self.prestamo.registrar_prestamo()

    def test_calcular_multa(self):
        self.prestamo.calcular_multa()
        # Lógica adicional para calcular multa

if __name__ == "__main__":
    unittest.main()
