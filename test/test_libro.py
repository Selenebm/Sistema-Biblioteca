import unittest
from articulos.libro import Libro

class TestLibro(unittest.TestCase):

    def setUp(self):
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

    def test_detalles(self):
        self.assertEqual(
            self.libro.detalles(),
            "Libro: Cien años de soledad, Autor: Gabriel García Márquez, Páginas: 471"
        )

    def test_consultar_disponibilidad(self):
        self.assertTrue(self.libro.consultar_disponibilidad())

    def test_actualizar_datos_articulo(self):
        self.libro.actualizar_datos_articulo(
            "El otoño del patriarca", "Gabriel García Márquez", 1975, 
            "Editorial Sudamericana", "978-3-16-148410-0", "Novela", 5
        )
        self.assertEqual(self.libro.titulo, "El otoño del patriarca")
        self.assertEqual(self.libro.num_ejemplares, 5)

if __name__ == "__main__":
    unittest.main()
