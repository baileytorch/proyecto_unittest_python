from importlib import import_module

from .conexion import base_datos, database

_REPOSITORIOS = {
    "cliente_por_id": "repo_cliente",
    "cliente_por_rut": "repo_cliente",
    "guardar_cliente": "repo_cliente",
    "listado_clientes": "repo_cliente",
    "listado_clientes_deshabilitados": "repo_cliente",
    "listado_clientes_habilitados": "repo_cliente",
    "detalle_pedido_por_id": "repo_detalle_pedido",
    "detalle_pedido_por_pedido": "repo_detalle_pedido",
    "guardar_detalle_pedido": "repo_detalle_pedido",
    "listado_detalle_pedidos": "repo_detalle_pedido",
    "listado_detalle_pedidos_deshabilitados": "repo_detalle_pedido",
    "listado_detalle_pedidos_habilitados": "repo_detalle_pedido",
    "guardar_pedido": "repo_pedido",
    "listado_pedidos": "repo_pedido",
    "listado_pedidos_deshabilitados": "repo_pedido",
    "listado_pedidos_habilitados": "repo_pedido",
    "pedido_por_id": "repo_pedido",
    "pedido_por_rut_cliente": "repo_pedido",
    "guardar_producto": "repo_producto",
    "listado_productos": "repo_producto",
    "listado_productos_deshabilitados": "repo_producto",
    "listado_productos_habilitados": "repo_producto",
    "producto_por_id": "repo_producto",
    "producto_por_sku": "repo_producto",
}

__all__ = ["base_datos", "database", *_REPOSITORIOS]


def __getattr__(nombre):
    modulo = _REPOSITORIOS.get(nombre)
    if modulo is None:
        raise AttributeError(f"module {__name__!r} has no attribute {nombre!r}")
    return getattr(import_module(f".{modulo}", __name__), nombre)
