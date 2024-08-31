import json
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from sistema_biblioteca import SistemaBiblioteca
from articulo import Articulo

# Ejemplo de uso
if __name__ == "__main__":
    sistema = SistemaBiblioteca()

    # Registrar bibliotecario
    bibliotecario = sistema.registrarBibliotecario("B001", "Ana Gómez", "Av. Siempre Viva 123", "555-1234", "ana@biblioteca.com", "1980-05-10", "Bibliotecario")

    # Registrar usuario
    usuario = sistema.registrarUsuario("usuario", "U001", "Juan Pérez", "Calle Falsa 456", "555-5678", "juan@ejemplo.com", "1990-11-20", "Estudiante")

    # Crear y agregar artículos al catálogo
    libro = Articulo("A001", "El Quijote", "Miguel de Cervantes", "1605", "Editorial XYZ", "978-3-16-148410-0", "Literatura", 5)
    revista = Articulo("A002", "Revista de Ciencia", "John Doe", "2024", "Editorial ABC", "978-1-23-456789-0", "Ciencia", 10)
    sistema.catalogo.agregarArticulo(libro)
    sistema.catalogo.agregarArticulo(revista)

    # Realizar un préstamo
    prestamo = sistema.realizarPrestamo(usuario, libro, 14)

    # Realizar una reserva
    reserva = sistema.realizarReserva(usuario, revista)

    # Devolver un artículo
    if prestamo:
        prestamo.devolver(datetime.now() + timedelta(days=2))