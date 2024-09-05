import unittest
from prestamos.notificacion import Notificacion
from prestamos.sujeto import Sujeto
from prestamos.observador import UsuarioObservador
from usuarios.usuario import Usuario

class TestNotificacion(unittest.TestCase):

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
        self.sujeto = Sujeto()
        self.observador = UsuarioObservador(self.usuario)
        self.sujeto.agregar_observador(self.observador)

    def test_notificar_observadores(self):
        self.sujeto.notificar_observadores("Nuevo préstamo disponible")
        # Verificar que el mensaje se notifica correctamente

if __name__ == "__main__":
    unittest.main()
