import re

from cliente_dao import ClienteDAO


def validar_opcion():
    """
    Solicita al usuario que ingrese una opción numérica entre 1 y 5 y valida la entrada.

    La función solicita repetidamente una opción al usuario hasta que se ingrese un número entero
    válido dentro del rango permitido (1-5). Si el valor ingresado está fuera de rango o no es un número,
    se muestra un mensaje de error y se solicita la entrada nuevamente.

    Returns:
        int: Un número entero entre 1 y 5 ingresado por el usuario.
    """
    while True:
        try:
            opcion = int(input('Escribe tu opción (1-5): '))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Por favor, selecciona un número entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")


def validar_entero(mensaje):
    """
    Solicita al usuario que ingrese un número entero y valida la entrada.

    La función solicita repetidamente una entrada al usuario hasta que se ingrese un número entero válido.
    Si la entrada no es un número entero, se muestra un mensaje de error y se solicita la entrada nuevamente.

    Args:
        mensaje (str): El mensaje que se muestra al usuario para ingresar un número.

    Returns:
        int: Un número entero ingresado por el usuario.
    """
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")


def validar_texto(mensaje):
    """
    Solicita al usuario que ingrese un texto y valida la entrada.

    La función solicita repetidamente un texto al usuario hasta que se ingresa un texto que no esté vacío
    y contenga solo letras y espacios. Se muestra un mensaje de error si el texto está vacío o contiene
    caracteres no permitidos.

    Args:
        mensaje (str): El mensaje que se muestra al usuario para ingresar el texto.

    Returns:
        str: El texto ingresado por el usuario.
    """
    while True:
        texto = input(mensaje).strip()
        if not texto:
            print("El texto no puede estar vacío. Por favor, inténtalo de nuevo.")
        elif not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ ]+$", texto):
            print("El texto solo puede contener letras y espacios. No se permiten números ni caracteres especiales.")
        else:
            return texto


def validar_numero(mensaje):
    """
    Solicita al usuario que ingrese un número positivo y valida la entrada.

    La función solicita repetidamente un valor al usuario hasta que se ingresa un número positivo. Si el valor
    ingresado no es un número o no es positivo, se muestra un mensaje de error y se solicita la entrada nuevamente.

    Args:
        mensaje (str): El mensaje que se muestra al usuario para ingresar el número.

    Returns:
        int: Un número entero positivo ingresado por el usuario.
    """
    while True:
        numero = input(mensaje).strip()
        if numero.isdigit():
            numero = int(numero)
            if numero > 0:
                return numero
            else:
                print("El número debe ser positivo.")
        else:
            print("Entrada inválida. Por favor, ingresa solo números positivos.")


def membresia_existe(membresia):
    """
    Verifica si una membresía existe en la base de datos de clientes.

    La función consulta la base de datos a través de `ClienteDAO` para determinar si la membresía proporcionada
    ya existe. Utiliza el método `buscar_por_membresia` del `ClienteDAO` para realizar la búsqueda.

    Args:
        membresia (str): El identificador de membresía a verificar.

    Returns:
        bool: `True` si la membresía existe en la base de datos, `False` en caso contrario.
    """
    return ClienteDAO.buscar_por_membresia(membresia) is not None
