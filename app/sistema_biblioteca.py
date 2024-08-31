from catalogo import Catalogo
from usuarioFactory import UsuarioFactory
from datetime import datetime, timedelta
from prestamo import Prestamo
from multa_retraso import EstrategiaCalculoMultaPorRetraso
from reserva import Reserva



class SistemaBiblioteca:
    def __init__(self):
        self.catalogo = Catalogo()
        self.usuarios = []
        self.prestamos = []
        self.reservas = []

    def registrarUsuario(self, tipo, ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion, **extra):
        usuario = UsuarioFactory.crearUsuario(tipo, ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion, **extra)
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombreCompleto} registrado con éxito.")
        return usuario

    def registrarBibliotecario(self, ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion):
        bibliotecario = UsuarioFactory.crearUsuario("bibliotecario", ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion)
        self.usuarios.append(bibliotecario)
        print(f"Bibliotecario {bibliotecario.nombreCompleto} registrado con éxito.")
        return bibliotecario

    def realizarPrestamo(self, usuario, articulo, diasPrestamo):
        if articulo.numEjemplares > 0:
            fechaPrestamo = datetime.now()
            fechaDevolucionEstimada = fechaPrestamo + timedelta(days=diasPrestamo)
            prestamo = Prestamo(
                ID=len(self.prestamos) + 1,
                usuario=usuario,
                articulo=articulo,
                fechaPrestamo=fechaPrestamo,
                fechaDevolucionEstimada=fechaDevolucionEstimada,
                estrategia_calculo_multa=EstrategiaCalculoMultaPorRetraso()
            )
            self.prestamos.append(prestamo)
            articulo.numEjemplares -= 1
            print(f"Préstamo realizado para el artículo {articulo.titulo} a {usuario.nombreCompleto}.")
            return prestamo
        else:
            print("No hay ejemplares disponibles para este artículo.")
            return None

    def realizarReserva(self, usuario, articulo):
        fechaReserva = datetime.now()
        reserva = Reserva(
            ID=len(self.reservas) + 1,
            usuario=usuario,
            articulo=articulo,
            fechaReserva=fechaReserva
        )
        self.reservas.append(reserva)
        print(f"Reserva realizada para el artículo {articulo.titulo} por {usuario.nombreCompleto}.")
        return reserva