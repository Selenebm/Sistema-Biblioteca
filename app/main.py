import json
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

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

# Factory Method - Creación de usuarios
class UsuarioFactory:
    @staticmethod
    def crearUsuario(tipo, ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion, **extra):
        if tipo == "usuario":
            return Usuario(ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion)
        elif tipo == "usuario_con_multa":
            return UsuarioConMulta(ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion, extra.get("multaPendiente", 0.0))
        elif tipo == "bibliotecario":
            return Bibliotecario(ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion)
        elif tipo == "estudiante":
            return Estudiante(ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion, extra.get("centroEstudios", ""))
        else:
            raise ValueError("Tipo de usuario no reconocido")

# Observer - Para manejar notificaciones
class Subject(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, mensaje):
        for observer in self._observers:
            observer.update(mensaje)

class Articulo(Subject):
    def __init__(self, ID, titulo, autor, fechaPublicacion, editorial, isbn, categoria, numEjemplares):
        super().__init__()
        self.ID = ID
        self.titulo = titulo
        self.autor = autor
        self.fechaPublicacion = fechaPublicacion
        self.editorial = editorial
        self.isbn = isbn
        self.categoria = categoria
        self.numEjemplares = numEjemplares

    def actualizarDatosArticulo(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        print(f"Datos del artículo {self.ID} actualizados con éxito.")
        self.notify_observers(f"El artículo {self.titulo} ha sido actualizado.")

    def to_dict(self):
        return {
            'ID': self.ID,
            'titulo': self.titulo,
            'autor': self.autor,
            'fechaPublicacion': self.fechaPublicacion,
            'editorial': self.editorial,
            'isbn': self.isbn,
            'categoria': self.categoria,
            'numEjemplares': self.numEjemplares
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            ID=data['ID'],
            titulo=data['titulo'],
            autor=data['autor'],
            fechaPublicacion=data['fechaPublicacion'],
            editorial=data['editorial'],
            isbn=data['isbn'],
            categoria=data['categoria'],
            numEjemplares=data['numEjemplares']
        )

class Notificacion:
    def update(self, mensaje):
        print(f"Notificación recibida: {mensaje}")

# Clases base para usuarios y sus variaciones
class Usuario:
    def __init__(self, ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion):
        self.ID = ID
        self.nombreCompleto = nombreCompleto
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fechaNacimiento = fechaNacimiento
        self.ocupacion = ocupacion

    def mostrarInformacion(self):
        print(f"ID: {self.ID}, Nombre: {self.nombreCompleto}, Email: {self.email}")

class UsuarioConMulta(Usuario):
    def __init__(self, ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion, multaPendiente):
        super().__init__(ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion)
        self.multaPendiente = multaPendiente

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Multa pendiente: {self.multaPendiente}")

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

class Estudiante(Usuario):
    def __init__(self, ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion, centroEstudios):
        super().__init__(ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion)
        self.centroEstudios = centroEstudios

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Centro de Estudios: {self.centroEstudios}")

# Clase Multa - Para gestionar multas
class Multa:
    def __init__(self, monto, fechaAplicacion):
        self.monto = monto
        self.fechaAplicacion = fechaAplicacion

    def mostrarMulta(self):
        print(f"Multa: {self.monto}, Fecha de Aplicación: {self.fechaAplicacion}")

# Clase Prestamo - Para gestionar préstamos
class Prestamo:
    def __init__(self, ID, usuario, articulo, fechaPrestamo, fechaDevolucionEstimada, estrategia_calculo_multa=None):
        self.ID = ID
        self.usuario = usuario
        self.articulo = articulo
        self.fechaPrestamo = fechaPrestamo
        self.fechaDevolucionEstimada = fechaDevolucionEstimada
        self.fechaDevolucion = None
        self.estrategia_calculo_multa = estrategia_calculo_multa

    def devolver(self, fechaDevolucion):
        self.fechaDevolucion = fechaDevolucion
        print(f"Artículo {self.articulo.titulo} devuelto por {self.usuario.nombreCompleto} el {self.fechaDevolucion}")
        self.calcularMulta()

    def calcularMulta(self):
        if self.estrategia_calculo_multa:
            return self.estrategia_calculo_multa.calcular(self)
        return 0.0

    def calcularRenovacion(self):
        print(f"Préstamo de {self.articulo.titulo} renovado.")

# Strategy - Clases para definir diferentes estrategias de cálculo de multas
class EstrategiaCalculoMulta(ABC):
    @abstractmethod
    def calcular(self, prestamo):
        pass

class EstrategiaCalculoMultaPorRetraso(EstrategiaCalculoMulta):
    def calcular(self, prestamo):
        if prestamo.fechaDevolucion and prestamo.fechaDevolucion > prestamo.fechaDevolucionEstimada:
            dias_retraso = (prestamo.fechaDevolucion - prestamo.fechaDevolucionEstimada).days
            multa = dias_retraso * 2.0  # Ejemplo: $2 por día de retraso
            print(f"Multa calculada: ${multa}")
            return multa
        return 0.0

class EstrategiaCalculoMultaFlexible(EstrategiaCalculoMulta):
    def calcular(self, prestamo):
        # Otra estrategia para calcular la multa que podría basarse en otros factores
        pass

# Clase Reserva - Para gestionar reservas de artículos
class Reserva:
    def __init__(self, ID, usuario, articulo, fechaReserva, estadoReserva="Activa"):
        self.ID = ID
        self.usuario = usuario
        self.articulo = articulo
        self.fechaReserva = fechaReserva
        self.estadoReserva = estadoReserva

    def cancelarReserva(self):
        self.estadoReserva = "Cancelada"
        print(f"Reserva de {self.articulo.titulo} cancelada.")

    def mostrarReserva(self):
        print(f"Reserva ID: {self.ID}, Usuario: {self.usuario.nombreCompleto}, Artículo: {self.articulo.titulo}, Fecha Reserva: {self.fechaReserva}, Estado: {self.estadoReserva}")

# Clase para gestionar préstamos y reservas
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