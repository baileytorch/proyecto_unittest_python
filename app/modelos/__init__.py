from importlib import import_module

_MODELOS = {
    "Cliente": "cliente",
    "DetallePedido": "detalle_pedido",
    "Pedido": "pedido",
    "Producto": "producto",
}

__all__ = list(_MODELOS)


def __getattr__(nombre):
    modulo = _MODELOS.get(nombre)
    if modulo is None:
        raise AttributeError(f"module {__name__!r} has no attribute {nombre!r}")
    return getattr(import_module(f".{modulo}", __name__), nombre)