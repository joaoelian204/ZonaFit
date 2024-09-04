from mysql.connector import Error, pooling


class Conexion:
    """
    Una clase que representa una conexión a la base de datos.
    Atributos:
        DATABASE (str): El nombre de la base de datos.
        USERNAME (str): El nombre de usuario para la conexión a la base de datos.
        PASSWORD (str): La contraseña para la conexión a la base de datos.
        DB_PORT (str): El número de puerto para la conexión a la base de datos.
        HOST (str): La dirección del host para la conexión a la base de datos.
        POOL_SIZE (int): El tamaño del grupo de conexiones.
        POOL_NAME (str): El nombre del grupo de conexiones.
        pool (object): El objeto del grupo de conexiones.
    Métodos:
        obtener_pool(): Devuelve el objeto del grupo de conexiones.
        obtener_conexion(): Devuelve una conexión a la base de datos desde el grupo de conexiones.
        liberar_conexion(conexion): Libera una conexión a la base de datos de vuelta al grupo de conexiones.
        
    """
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'root'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:  # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                #print(f'Nombre del pool: {cls.pool.pool_name}')
                #print(f'Tamanio del pool: {cls.pool.pool_size}')
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()

