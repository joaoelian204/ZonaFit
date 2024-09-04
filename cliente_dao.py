from cliente import Cliente
from conexion import Conexion


class ClienteDAO:
    """
    Esta clase representa un Objeto de Acceso a Datos (DAO) para la tabla 'cliente' en una base de datos.
    Proporciona métodos para seleccionar, insertar, actualizar y eliminar registros de cliente.
    Atributos:
        SELECCIONAR (str): Consulta SQL para seleccionar todos los registros de cliente.
        INSERTAR (str): Consulta SQL para insertar un nuevo registro de cliente.
        ACTUALIZAR (str): Consulta SQL para actualizar un registro de cliente existente.
        ELIMINAR (str): Consulta SQL para eliminar un registro de cliente por su ID.
        BUSCAR_POR_MEMBRESIA (str): Consulta SQL para buscar un registro de cliente por su membresía.
    Métodos:
        seleccionar(): Selecciona todos los registros de cliente de la base de datos y los devuelve como una lista de objetos Cliente.
        insertar(cliente): Inserta un nuevo registro de cliente en la base de datos.
        actualizar(cliente): Actualiza un registro de cliente existente en la base de datos.
        eliminar(cliente): Elimina un registro de cliente de la base de datos.
        buscar_por_membresia(membresia): Busca un registro de cliente por su membresía y lo devuelve como un objeto Cliente.
        
    """
    SELECCIONAR = 'SELECT * FROM cliente'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'
    BUSCAR_POR_MEMBRESIA = 'SELECT * FROM cliente WHERE membresia=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def buscar_por_membresia(cls, membresia):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.BUSCAR_POR_MEMBRESIA, (membresia,))
            registro = cursor.fetchone()
            if registro:
                return Cliente(registro[0], registro[1], registro[2], registro[3])
            return None
        except Exception as e:
            print(f'Ocurrio un error al buscar por membresía: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

                
