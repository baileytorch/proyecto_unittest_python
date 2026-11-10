from ..modelos.detalle_pedido import DetallePedido
from ..modelos.pedido import Pedido

def listado_detalle_pedidos_habilitados():
    try:
        detalle_pedidos = DetallePedido.select().where(DetallePedido.habilitado == True)
        return detalle_pedidos
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def listado_detalle_pedidos_deshabilitados():
    try:
        detalle_pedidos = DetallePedido.select().where(DetallePedido.habilitado == False)
        return detalle_pedidos
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def listado_detalle_pedidos():
    try:
        detalle_pedidos = DetallePedido.select()
        return detalle_pedidos
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def guardar_detalle_pedido(detalle_pedido: DetallePedido):
    try:
        nuevo_detalle_pedido = detalle_pedido.save()
        return nuevo_detalle_pedido
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def detalle_pedido_por_pedido(id_pedido):
    try:
        detalle_pedido = DetallePedido.select().join(Pedido).where(Pedido.id_pedido == id_pedido)
        return detalle_pedido
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def detalle_pedido_por_id(id):
    try:
        detalle_pedido = DetallePedido[id]
        if detalle_pedido:
            return detalle_pedido
    except DetallePedido.DoesNotExist:
        print('El Detalle de Pedido indicado NO existe.')
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')