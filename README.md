# Sistema de Gestión de Bibliotecas

## Descripción

Este proyecto es un sistema de gestión de bibliotecas en Python que permite manejar usuarios, bibliotecarios, artículos (libros, revistas, CD, etc.), préstamos, reservas y multas. Utiliza patrones de diseño como Singleton, Factory Method, Observer y Strategy para manejar las diversas funcionalidades.

## Funcionalidades

- **Gestión de Usuarios y Bibliotecarios:** Registro y gestión de usuarios (incluyendo usuarios con multas) y bibliotecarios.
- **Gestión de Artículos:** Agregar, eliminar y buscar artículos en el catálogo.
- **Préstamos y Reservas:** Realizar y gestionar préstamos y reservas de artículos.
- **Cálculo de Multas:** Estrategias para calcular multas por retraso en la devolución de artículos.
- **Notificaciones:** Sistema de notificación para actualizar sobre cambios en los artículos.

## Instalación

Para utilizar este sistema, necesitas tener Python 3.8 o superior instalado.

1. **Clona el Repositorio:**

    ```bash
    https://github.com/Selenebm/Sistema-Biblioteca.git
    ```

2. **Instala las Dependencias (si es necesario):**

    No hay dependencias externas requeridas para este proyecto. Python estándar es suficiente.

## Uso

1. **Ejecución del Script Principal:**

    Puedes ejecutar el script principal `sistema-biblioteca.py` para utilizar el sistema. Este script incluye ejemplos de cómo registrar usuarios, bibliotecarios, agregar artículos, realizar préstamos y reservas.

    ```bash
    python sistema-biblioteca.py
    ```

2. **Métodos y Funcionalidades:**

    - **Registrar Usuario:**

        ```python
        sistema.registrarUsuario(tipo, ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion, **extra)
        ```

    - **Registrar Bibliotecario:**

        ```python
        sistema.registrarBibliotecario(ID, nombreCompleto, direccion, telefono, email, fechaNacimiento, ocupacion)
        ```

    - **Agregar Artículo:**

        ```python
        catalogo.agregarArticulo(articulo)
        ```

    - **Realizar Préstamo:**

        ```python
        sistema.realizarPrestamo(usuario, articulo, diasPrestamo)
        ```

    - **Realizar Reserva:**

        ```python
        sistema.realizarReserva(usuario, articulo)
        ```

    - **Devolver Artículo:**

        ```python
        prestamo.devolver(fechaDevolucion)
        ```

## Contribución

¡Las contribuciones son bienvenidas! Para contribuir:

1. **Haz un Fork del Repositorio.**
2. **Crea una Nueva Rama:**

    ```bash
    git checkout -b mi-nueva-rama
    ```

3. **Haz tus Cambios.**
4. **Haz Commit y Push de tus Cambios:**

    ```bash
    git add .
    git commit -m "Descripción de los cambios"
    git push origin mi-nueva-rama
    ```
