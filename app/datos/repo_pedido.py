from ..modelos.cliente import Cliente
from ..modelos.pedido import Pedido

def listado_pedidos_habilitados():
    try:
        pedidos = Pedido.select().where(Pedido.pedido_habilitado == True)
        return pedidos
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def listado_pedidos_deshabilitados():
    try:
        pedidos = Pedido.select().where(Pedido.pedido_habilitado == False)
        return pedidos
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def listado_pedidos():
    try:
        pedidos = Pedido.select()
        return pedidos
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def guardar_pedido(pedido: Pedido):
    try:
        nuevo_pedido = pedido.save()
        return nuevo_pedido
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def pedido_por_rut_cliente(rut):
    try:
        pedidos = Pedido.select().join(Cliente).where(Cliente.rut_cliente == rut)
        return pedidos
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def pedido_por_id(id):
    try:
        pedido = Pedido[id]
        if pedido:
            return pedido
    except Pedido.DoesNotExist:
        print('El pedido indicado NO existe.')
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')