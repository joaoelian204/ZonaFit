from cliente import Cliente
from cliente_dao import ClienteDAO
from validaciones import (
    membresia_existe,
    validar_entero,
    validar_numero,
    validar_texto,
)


def listar_clientes():
    clientes = ClienteDAO.seleccionar()
    if clientes:
        print('\n*** Listado de Clientes ***')
        for cliente in clientes:
            print(cliente)
    else:
        print("No hay clientes registrados.")
    print()

def agregar_cliente():
    nombre = validar_texto('Escribe el nombre: ')
    apellido = validar_texto('Escribe el apellido: ')
    while True:
        membresia = validar_numero('Escribe la membresía (solo números positivos): ')
        if membresia_existe(membresia):
            print(f"La membresía {membresia} ya está en uso. Por favor, elige otra membresia.")
        else:
            break
    cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
    try:
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}')
    except Exception as e:
        print(f'Ocurrió un error al insertar cliente: {e}')

def modificar_cliente():
    if not ClienteDAO.seleccionar():  # Verifica que haya clientes registrados
        print("No hay clientes para modificar.")
        return
    id_cliente = validar_entero('Escribe el id del cliente a modificar: ')
    nombre = validar_texto('Escribe el nombre: ')
    apellido = validar_texto('Escribe el apellido: ')
    membresia = validar_numero('Escribe la membresía (solo números positivos): ')
    cliente = Cliente(id=id_cliente, nombre=nombre, apellido=apellido, membresia=membresia)
    try:
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f'Clientes actualizados: {clientes_actualizados}')
    except Exception as e:
        print(f'Ocurrió un error al actualizar cliente: {e}')

def eliminar_cliente():
    if not ClienteDAO.seleccionar():  # Verifica que haya clientes registrados
        print("No hay clientes para eliminar.")
        return
    id_cliente = validar_entero('Escribe el id del cliente a eliminar: ')
    cliente = Cliente(id=id_cliente)
    try:
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f'Clientes eliminados: {clientes_eliminados}')
    except Exception as e:
        print(f'Ocurrió un error al eliminar cliente: {e}')

def mostrar_menu():
    print('''
*** Clientes de Zona Fit (GYM) ***
Menu:
1. Listar clientes
2. Agregar cliente
3. Modificar cliente
4. Eliminar cliente
5. Salir''')