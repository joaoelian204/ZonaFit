from funciones import (
    agregar_cliente,
    eliminar_cliente,
    listar_clientes,
    modificar_cliente,
    mostrar_menu,
)
from validaciones import validar_opcion


def main():
    opcion = None
    while opcion != 5:
        mostrar_menu()
        opcion = validar_opcion()
        if opcion == 1:
            listar_clientes()
        elif opcion == 2:
            agregar_cliente()
        elif opcion == 3:
            modificar_cliente()
        elif opcion == 4:
            eliminar_cliente()
        elif opcion == 5:
            print('Salimos de la aplicación...')
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")
    print('Aplicación cerrada, muchas gracias por su tiempo.')

if __name__ == '__main__':
    main()
