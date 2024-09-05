from usuarios.usuario import Usuario
from usuarios.bibliotecario import Bibliotecario
from articulos.libro import Libro
from articulos.revista import Revista
from prestamos.prestamo import Prestamo
from prestamos.reserva import Reserva
from prestamos.notificacion import Notificacion
from catalogo.catalogo import Catalogo
from reportes.reporte import Reporte
from sugerencias.sugerencia import Sugerencia

def mostrar_menu():
    print("\n----- Menú de la Biblioteca -----")
    print("1. Registrar Usuario")
    print("2. Registrar Bibliotecario")
    print("3. Agregar Artículo al Catálogo")
    print("4. Realizar Préstamo")
    print("5. Realizar Reserva")
    print("6. Generar Reporte")
    print("7. Enviar Sugerencia")
    print("8. Salir")
    return input("Seleccione una opción: ")

def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    id_usuario = input("ID del Usuario: ")
    nombre = input("Nombre completo: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
    ocupacion = input("Ocupación: ")
    
    usuario = Usuario(
        id=id_usuario, nombre_completo=nombre, direccion=direccion,
        telefono=telefono, email=email, fecha_nacimiento=fecha_nacimiento,
        ocupacion=ocupacion
    )
    usuario.registrar_usuario()
    print(f"Usuario {nombre} registrado exitosamente.")
    return usuario

def registrar_bibliotecario():
    print("\n--- Registro de Bibliotecario ---")
    bibliotecario = registrar_usuario()
    bibliotecario = Bibliotecario(**vars(bibliotecario))
    print(f"Bibliotecario {bibliotecario.nombre_completo} registrado exitosamente.")
    return bibliotecario

def agregar_articulo(catalogo):
    print("\n--- Agregar Artículo ---")
    tipo_articulo = input("Tipo de artículo (Libro/Revista): ")
    id_articulo = input("ID del artículo: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = input("Año de publicación: ")
    editorial = input("Editorial: ")
    categoria = input("Categoría: ")
    num_ejemplares = int(input("Número de ejemplares: "))

    if tipo_articulo.lower() == "libro":
        num_paginas = int(input("Número de páginas: "))
        genero = input("Género: ")
        formato = input("Formato (Tapa dura, etc.): ")
        libro = Libro(
            id=id_articulo, titulo=titulo, autor=autor, anio_publicacion=anio,
            editorial=editorial, categoria=categoria, num_ejemplares=num_ejemplares,
            num_paginas=num_paginas, genero=genero, formato=formato
        )
        catalogo.agregar_articulo(libro)
        print(f"Libro '{titulo}' agregado al catálogo.")
    elif tipo_articulo.lower() == "revista":
        numero_edicion = int(input("Número de edición: "))
        mes_publicacion = input("Mes de publicación: ")
        tema_principal = input("Tema principal: ")
        revista = Revista(
            id=id_articulo, titulo=titulo, autor=autor, anio_publicacion=anio,
            editorial=editorial, categoria=categoria, num_ejemplares=num_ejemplares,
            numero_edicion=numero_edicion, mes_publicacion=mes_publicacion,
            tema_principal=tema_principal
        )
        catalogo.agregar_articulo(revista)
        print(f"Revista '{titulo}' agregada al catálogo.")

def realizar_prestamo(usuario, catalogo):
    print("\n--- Realizar Préstamo ---")
    id_prestamo = input("ID del Préstamo: ")
    id_articulo = input("ID del Artículo a prestar: ")
    articulo = catalogo.buscar_articulo(id_articulo)

    if articulo and articulo.consultar_disponibilidad():
        fecha_prestamo = input("Fecha de Préstamo (YYYY-MM-DD): ")
        fecha_devolucion_estimada = input("Fecha de Devolución Estimada (YYYY-MM-DD): ")
        tipo_prestamo = input("Tipo de Préstamo (Corto/Largo plazo): ")
        prestamo = Prestamo(
            id_prestamo=id_prestamo,
            usuario=usuario,
            articulo=articulo,
            fecha_prestamo=fecha_prestamo,
            fecha_devolucion_estimada=fecha_devolucion_estimada,
            tipo_prestamo=tipo_prestamo
        )
        prestamo.registrar_prestamo()
        print(f"Préstamo del artículo '{articulo.titulo}' registrado exitosamente.")
    else:
        print("El artículo no está disponible o no existe.")

def realizar_reserva(usuario, catalogo):
    print("\n--- Realizar Reserva ---")
    id_reserva = input("ID de la Reserva: ")
    id_articulo = input("ID del Artículo a reservar: ")
    articulo = catalogo.buscar_articulo(id_articulo)

    if articulo:
        fecha_reserva = input("Fecha de Reserva (YYYY-MM-DD): ")
        reserva = Reserva(
            id_reserva=id_reserva,
            usuario=usuario,
            articulo=articulo,
            fecha_reserva=fecha_reserva
        )
        reserva.registrar_reserva()
        print(f"Reserva del artículo '{articulo.titulo}' registrada exitosamente.")
    else:
        print("El artículo no existe.")

def generar_reporte(catalogo):
    print("\n--- Generar Reporte ---")
    tipo_reporte = input("Tipo de Reporte (General/Categoría): ")
    reporte = Reporte(id_reporte="r001", tipo_reporte=tipo_reporte, datos=catalogo.articulos)
    reporte.generar_reporte()
    print("Reporte generado exitosamente.")

def enviar_sugerencia(usuario):
    print("\n--- Enviar Sugerencia ---")
    id_sugerencia = input("ID de la Sugerencia: ")
    mensaje = input("Mensaje de la Sugerencia: ")
    sugerencia = Sugerencia(
        id_sugerencia=id_sugerencia,
        usuario=usuario,
        mensaje=mensaje
    )
    sugerencia.enviar_sugerencia()
    print("Sugerencia enviada exitosamente.")

def main():
    catalogo = Catalogo()
    usuario = None
    bibliotecario = None

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            usuario = registrar_usuario()
        elif opcion == "2":
            bibliotecario = registrar_bibliotecario()
        elif opcion == "3" and bibliotecario:
            agregar_articulo(catalogo)
        elif opcion == "4" and usuario:
            realizar_prestamo(usuario, catalogo)
        elif opcion == "5" and usuario:
            realizar_reserva(usuario, catalogo)
        elif opcion == "6":
            generar_reporte(catalogo)
        elif opcion == "7" and usuario:
            enviar_sugerencia(usuario)
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida o falta de permisos (Debe registrarse un usuario o bibliotecario).")

if __name__ == "__main__":
    main()
