class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        """
        Inicializa una nueva instancia de la clase Cliente.

        Args:
            id (int, optional): El identificador único del cliente. Por defecto es None.
            nombre (str, optional): El nombre del cliente. Por defecto es None.
            apellido (str, optional): El apellido del cliente. Por defecto es None.
            membresia (str, optional): El identificador de membresía del cliente. Por defecto es None.
        """
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        """
        Devuelve una representación en cadena del cliente.

        La representación en cadena incluye el identificador, nombre, apellido y membresía del cliente.

        Returns:
            str: Una cadena que describe al cliente en el formato "Id: <id>, Nombre: <nombre>, Apellido: <apellido>, Membresia: <membresia>".
        """
        return (f'Id: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')