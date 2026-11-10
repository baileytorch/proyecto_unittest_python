from decimal import Decimal

from prettytable import PrettyTable

from ..datos.conexion import base_datos
from ..datos.repo_detalle_pedido import (
    listado_detalle_pedidos_habilitados,
    detalle_pedido_por_pedido,
    guardar_detalle_pedido,
)
from ..datos.repo_pedido import guardar_pedido
from ..modelos.detalle_pedido import DetallePedido
from ..modelos.pedido import Pedido
from ..modelos.producto import Producto


def cargar_detalle_pedidos(tabla: PrettyTable):
    detalles = listado_detalle_pedidos_habilitados()
    tabla.field_names = ["Id", "Pedido", "SKU", "Producto", "Cantidad", "Precio", "Subtotal"]

    for detalle in detalles:
        precio = detalle.precio_unitario
        tabla.add_row([
            detalle.id_detalle_pedido,
            detalle.id_pedido.id_pedido,
            detalle.id_producto.sku_producto,
            detalle.id_producto.nombre_producto,
            detalle.cantidad,
            precio,
            precio * detalle.cantidad,
        ])

    return tabla


def cargar_detalle_pedido_por_pedido(tabla: PrettyTable, id_pedido: int):
    detalles = detalle_pedido_por_pedido(id_pedido)
    tabla.field_names = ["Id", "Pedido", "SKU", "Producto", "Cantidad", "Precio", "Subtotal"]

    if detalles is not None:
        for detalle in detalles:
            precio = detalle.precio_unitario
            tabla.add_row([
                detalle.id_detalle_pedido,
                detalle.id_pedido.id_pedido,
                detalle.id_producto.sku_producto,
                detalle.id_producto.nombre_producto,
                detalle.cantidad,
                precio,
                precio * detalle.cantidad,
            ])

    return tabla


def crear_detalle_pedido(pedido: Pedido, producto: Producto, cantidad: int):
    _validar_cantidad(cantidad)
    nuevo_detalle = DetallePedido()
    nuevo_detalle.id_pedido = pedido
    nuevo_detalle.id_producto = producto
    nuevo_detalle.cantidad = cantidad
    nuevo_detalle.precio_unitario = producto.precio_producto or Decimal("0.00")
    nuevo_detalle.habilitado = True

    with base_datos().atomic():
        respuesta = guardar_detalle_pedido(nuevo_detalle)
        if not respuesta:
            raise RuntimeError("No se pudo guardar el detalle del pedido.")
        _recalcular_total_pedido(pedido)

    print(f"Detalle de pedido {nuevo_detalle.id_detalle_pedido} guardado con éxito.")
    return nuevo_detalle


def modificar_detalle_pedido(
    detalle: DetallePedido,
    pedido: Pedido,
    producto: Producto,
    cantidad: int,
):
    _validar_cantidad(cantidad)
    pedido_anterior = detalle.id_pedido
    if detalle.id_pedido != pedido:
        detalle.id_pedido = pedido
    if detalle.id_producto != producto:
        detalle.id_producto = producto
        detalle.precio_unitario = producto.precio_producto or Decimal("0.00")
    if detalle.cantidad != cantidad:
        detalle.cantidad = cantidad

    with base_datos().atomic():
        respuesta = guardar_detalle_pedido(detalle)
        if not respuesta:
            raise RuntimeError("No se pudo guardar el detalle del pedido.")
        _recalcular_total_pedido(pedido_anterior)
        if pedido_anterior.get_id() != pedido.get_id():
            _recalcular_total_pedido(pedido)

    print(f"Detalle de pedido {detalle.id_detalle_pedido} modificado con éxito.")
    return detalle


def _validar_cantidad(cantidad: int):
    if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
        raise ValueError("La cantidad debe ser un entero mayor que cero.")


def _recalcular_total_pedido(pedido: Pedido):
    detalles = detalle_pedido_por_pedido(pedido.id_pedido)
    if detalles is None:
        raise RuntimeError("No se pudieron consultar los detalles del pedido.")

    pedido.total_pedido = sum(
        (
            detalle.precio_unitario * detalle.cantidad
            for detalle in detalles
            if detalle.habilitado
        ),
        Decimal("0.00"),
    )
    if not guardar_pedido(pedido):
        raise RuntimeError("No se pudo actualizar el total del pedido.")
