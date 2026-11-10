from prettytable import PrettyTable

from ..datos import detalle_pedido_por_id, pedido_por_id, producto_por_sku
from ..negocio import (
    cargar_detalle_pedido_por_pedido,
    cargar_detalle_pedidos,
    crear_detalle_pedido,
    modificar_detalle_pedido,
)
from ..auxiliares import error_generico


def listado_detalle_pedidos():
    print("LISTADO DE DETALLES DE PEDIDO")
    print("=============================")
    try:
        print(cargar_detalle_pedidos(PrettyTable()))
    except Exception as error:
        print(f"{error_generico} {error}")


def listado_detalle_pedido_por_pedido():
    try:
        id_pedido = int(input("ID del pedido: ").strip())
        print(cargar_detalle_pedido_por_pedido(PrettyTable(), id_pedido))
    except ValueError:
        print("El ID del pedido debe ser numérico.")
    except Exception as error:
        print(f"{error_generico} {error}")


def ingresar_detalle_pedido():
    print("AGREGAR DETALLE DE PEDIDO")
    print("=========================")
    try:
        pedido = _buscar_pedido(input("ID del pedido: ").strip())
        if pedido is None:
            print("Pedido NO encontrado.")
            return

        producto = _buscar_producto(
            input("SKU del producto: ").strip()
        )
        if producto is None:
            print("Producto NO encontrado.")
            return

        cantidad = _solicitar_cantidad()
        crear_detalle_pedido(pedido, producto, cantidad)
    except Exception as error:
        print(f"{error_generico} {error}")


def actualizar_detalle_pedido():
    print("MODIFICAR DETALLE DE PEDIDO")
    print("===========================")
    try:
        id_detalle = int(input("ID del detalle a modificar: ").strip())
        detalle = detalle_pedido_por_id(id_detalle)
        if detalle is None:
            print("Detalle de pedido NO encontrado.")
            return

        print(PrettyTable(
            ["ID", "ID Pedido", "SKU Producto", "Cantidad"],
            [[detalle.id_detalle_pedido, detalle.id_pedido.id_pedido,
              detalle.id_producto.sku_producto, detalle.cantidad]],
        ))

        id_pedido = input(
            "Nuevo ID de pedido "
            f"(ENTER para mantener {detalle.id_pedido.id_pedido}): "
        ).strip()
        pedido = (
            _buscar_pedido(id_pedido)
            if id_pedido
            else detalle.id_pedido
        )
        if pedido is None:
            print("Pedido NO encontrado; el detalle no fue modificado.")
            return

        sku = input(
            "Nuevo SKU de producto "
            f"(ENTER para mantener {detalle.id_producto.sku_producto}): "
        ).strip()
        producto = _buscar_producto(sku) if sku else detalle.id_producto
        if producto is None:
            print("Producto NO encontrado; el detalle no fue modificado.")
            return

        cantidad_ingresada = input(
            f"Nueva cantidad (ENTER para mantener {detalle.cantidad}): "
        ).strip()
        cantidad = (
            _convertir_cantidad(cantidad_ingresada)
            if cantidad_ingresada
            else detalle.cantidad
        )

        modificar_detalle_pedido(detalle, pedido, producto, cantidad)
    except ValueError as error:
        print(f"El dato ingresado no es válido: {error}")
    except Exception as error:
        print(f"{error_generico} {error}")


def _buscar_pedido(valor: str):
    return pedido_por_id(int(valor))


def _buscar_producto(sku: str):
    productos = producto_por_sku(sku)
    return productos.first() if productos is not None else None


def _solicitar_cantidad() -> int:
    while True:
        try:
            return _convertir_cantidad(input("Cantidad: ").strip())
        except ValueError:
            print("Ingrese una cantidad entera mayor que cero.")


def _convertir_cantidad(valor: str) -> int:
    cantidad = int(valor)
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")
    return cantidad
