import unittest
from usuarios.usuario import Usuario

class TestUsuario(unittest.TestCase):

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

    def test_registrar_usuario(self):
        self.usuario.registrar_usuario()
        # Aquí puedes verificar si el método se ejecuta correctamente

    def test_validar_identificacion(self):
        self.assertTrue(self.usuario.validar_identificacion())

    def test_actualizar_datos(self):
        self.usuario.actualizar_datos(
            direccion="Calle Verdadera 456",
            telefono="555-5678",
            email="nuevo_email@example.com"
        )
        self.assertEqual(self.usuario.direccion, "Calle Verdadera 456")
        self.assertEqual(self.usuario.email, "nuevo_email@example.com")

if __name__ == "__main__":
    unittest.main()
