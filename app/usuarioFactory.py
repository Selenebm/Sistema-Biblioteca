from usuario import Usuario
from usuario_con_multa import UsuarioConMulta
from bibliotecario import Bibliotecario
from estudiante import Estudiante

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