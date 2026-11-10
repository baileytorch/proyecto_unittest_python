from .pres_cliente import actualizar_cliente, ingresar_cliente, listado_clientes
from .pres_detalle_pedido import (
    actualizar_detalle_pedido,
    ingresar_detalle_pedido,
    listado_detalle_pedido_por_pedido,
    listado_detalle_pedidos,
)
from .pres_pedido import (
    actualizar_pedido,
    ingresar_pedido,
    listado_pedidos,
    listado_pedidos_cliente,
)
from .pres_producto import actualizar_producto, ingresar_producto, listado_productos


def iniciar_menu():
    while True:
        print("\n=== SISTEMA DE GESTIÓN ===")
        print("1. Clientes")
        print("2. Productos")
        print("3. Pedidos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            print("Saliendo del sistema...")
            return
        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_productos()
        elif opcion == "3":
            menu_pedidos()
        else:
            print("Opción inválida.")


def menu_clientes():
    acciones = {
        "1": ("Listar clientes", listado_clientes),
        "2": ("Agregar cliente", ingresar_cliente),
        "3": ("Modificar cliente", actualizar_cliente),
    }

    while True:
        print("\n=== MENÚ DE CLIENTES ===")
        for numero, (etiqueta, _) in acciones.items():
            print(f"{numero}. {etiqueta}")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            return
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida.")
        else:
            accion[1]()


def menu_productos():
    acciones = {
        "1": ("Listar productos", listado_productos),
        "2": ("Agregar producto", ingresar_producto),
        "3": ("Modificar producto", actualizar_producto),
    }

    while True:
        print("\n=== MENÚ DE PRODUCTOS ===")
        for numero, (etiqueta, _) in acciones.items():
            print(f"{numero}. {etiqueta}")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            return
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida.")
        else:
            accion[1]()


def menu_pedidos():
    acciones = {
        "1": ("Listar pedidos", listado_pedidos),
        "2": ("Listar pedidos por cliente", listado_pedidos_cliente),
        "3": ("Agregar pedido", ingresar_pedido),
        "4": ("Modificar pedido", actualizar_pedido),
        "5": ("Listar detalles de pedido", listado_detalle_pedidos),
        "6": ("Listar detalles por pedido", listado_detalle_pedido_por_pedido),
        "7": ("Agregar detalle a pedido", ingresar_detalle_pedido),
        "8": ("Modificar detalle de pedido", actualizar_detalle_pedido),
    }

    while True:
        print("\n=== MENÚ DE PEDIDOS ===")
        for numero, (etiqueta, _) in acciones.items():
            print(f"{numero}. {etiqueta}")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            return
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida.")
        else:
            accion[1]()
