from decimal import Decimal

from prettytable import PrettyTable

from ..datos.repo_pedido import (
    listado_pedidos_habilitados,
    pedido_por_rut_cliente,
    guardar_pedido,
)
from ..modelos.cliente import Cliente
from ..modelos.pedido import EstadoPedido, Pedido


def cargar_pedidos(tabla: PrettyTable):
    pedidos = listado_pedidos_habilitados()
    tabla.field_names = ["Id", "RUT Cliente", "Fecha", "Total", "Estado"]

    for pedido in pedidos:
        tabla.add_row([
            pedido.id_pedido,
            pedido.cliente_pedido.rut_cliente,
            pedido.fecha_pedido,
            pedido.total_pedido,
            pedido.estado_pedido.value,
        ])

    return tabla


def cargar_pedidos_cliente(tabla: PrettyTable, rut_cliente: str):
    pedidos = pedido_por_rut_cliente(rut_cliente)
    tabla.field_names = ["Id", "RUT Cliente", "Fecha", "Total", "Estado"]

    if pedidos is not None:
        for pedido in pedidos:
            tabla.add_row([
                pedido.id_pedido,
                pedido.cliente_pedido.rut_cliente,
                pedido.fecha_pedido,
                pedido.total_pedido,
                pedido.estado_pedido.value,
            ])

    return tabla


def crear_pedido(
    cliente: Cliente,
    estado: EstadoPedido = EstadoPedido.PEND,
):
    nuevo_pedido = Pedido()
    nuevo_pedido.cliente_pedido = cliente
    nuevo_pedido.total_pedido = Decimal("0.00")
    nuevo_pedido.estado_pedido = estado
    nuevo_pedido.pedido_habilitado = True

    respuesta = guardar_pedido(nuevo_pedido)
    if respuesta:
        print(f"Pedido {nuevo_pedido.id_pedido} guardado con éxito.")
        return nuevo_pedido
    return None


def modificar_pedido(pedido: Pedido, cliente: Cliente, estado: EstadoPedido):
    if pedido.cliente_pedido != cliente:
        pedido.cliente_pedido = cliente
    if pedido.estado_pedido != estado:
        pedido.estado_pedido = estado

    respuesta = guardar_pedido(pedido)
    if respuesta:
        print(f"Pedido {pedido.id_pedido} modificado con éxito.")
