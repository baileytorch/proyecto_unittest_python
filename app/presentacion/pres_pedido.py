from prettytable import PrettyTable

from ..datos import cliente_por_rut, pedido_por_id, producto_por_sku
from ..negocio import (
    cargar_pedidos,
    cargar_pedidos_cliente,
    crear_pedido,
    crear_detalle_pedido,
    modificar_pedido,
)
from ..auxiliares import error_generico
from ..modelos.pedido import EstadoPedido


def listado_pedidos():
    print("LISTADO DE PEDIDOS")
    print("==================")
    try:
        print(cargar_pedidos(PrettyTable()))
    except Exception as error:
        print(f"{error_generico} {error}")


def listado_pedidos_cliente():
    rut = input("Ingrese el RUT del cliente: ").strip()
    try:
        print(cargar_pedidos_cliente(PrettyTable(), rut))
    except Exception as error:
        print(f"{error_generico} {error}")


def ingresar_pedido():
    print("AGREGAR PEDIDO")
    print("==============")
    try:
        cliente = _buscar_cliente(
            input("RUT del cliente para el pedido: ").strip()
        )
        if cliente is None:
            print("Cliente NO encontrado.")
            return

        estado = _solicitar_estado(EstadoPedido.PEND)
        pedido = crear_pedido(cliente, estado)
        if pedido is None:
            print("No se pudo crear el pedido.")
            return

        print(f"Pedido {pedido.id_pedido} creado con total inicial $0.00.")
        _agregar_productos_pedido(pedido)
    except Exception as error:
        print(f"{error_generico} {error}")


def actualizar_pedido():
    print("MODIFICAR PEDIDO")
    print("================")
    try:
        id_pedido = int(input("ID del pedido a modificar: ").strip())
        pedido = pedido_por_id(id_pedido)
        if pedido is None:
            print("Pedido NO encontrado.")
            return

        print(PrettyTable(
            ["ID", "RUT Cliente", "Fecha", "Total", "Estado"],
            [[pedido.id_pedido, pedido.cliente_pedido.rut_cliente,
              pedido.fecha_pedido, pedido.total_pedido,
              pedido.estado_pedido.value]],
        ))

        rut = input(
            "Nuevo RUT de cliente "
            f"(ENTER para mantener {pedido.cliente_pedido.rut_cliente}): "
        ).strip()
        cliente = _buscar_cliente(rut) if rut else pedido.cliente_pedido
        if cliente is None:
            print("Cliente NO encontrado; el pedido no fue modificado.")
            return

        estado = _solicitar_estado(pedido.estado_pedido)

        modificar_pedido(pedido, cliente, estado)
    except ValueError as error:
        print(f"El dato ingresado no es válido: {error}")
    except Exception as error:
        print(f"{error_generico} {error}")


def _buscar_cliente(rut: str):
    clientes = cliente_por_rut(rut)
    return clientes.first() if clientes is not None else None


def _agregar_productos_pedido(pedido):
    while True:
        sku = input("SKU del producto (ENTER para terminar el pedido): ").strip()
        if not sku:
            break

        productos = producto_por_sku(sku)
        producto = productos.first() if productos is not None else None
        if producto is None:
            print("Producto NO encontrado.")
            continue

        while True:
            try:
                cantidad = int(input("Cantidad: ").strip())
                if cantidad <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese una cantidad entera mayor que cero.")

        try:
            crear_detalle_pedido(pedido, producto, cantidad)
            print(f"Total actual del pedido: ${pedido.total_pedido}")
        except Exception as error:
            print(f"{error_generico} {error}")
    print(f"Pedido {pedido.id_pedido} finalizado con total ${pedido.total_pedido}.")


def _solicitar_estado(actual: EstadoPedido) -> EstadoPedido:
    estados = list(EstadoPedido)
    print("Estados disponibles:")
    for indice, estado in enumerate(estados, start=1):
        print(f"{indice}. {estado.value}")

    while True:
        valor = input(
            f"Seleccione estado (ENTER para mantener {actual.value}): "
        ).strip()
        if not valor:
            return actual
        try:
            return estados[int(valor) - 1]
        except (ValueError, IndexError):
            print("Seleccione un número de estado válido.")
