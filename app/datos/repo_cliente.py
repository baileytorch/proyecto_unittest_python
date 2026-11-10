from ..modelos.cliente import Cliente
from ..auxiliares import error_generico

def listado_clientes_habilitados():
    clientes = Cliente.select().where(Cliente.cliente_habilitado == True)
    return clientes

def listado_clientes_deshabilitados():
    clientes = Cliente.select().where(Cliente.cliente_habilitado == False)
    return clientes

def listado_clientes():
    clientes = Cliente.select()
    return clientes

def guardar_cliente(cliente: Cliente):
    try:
        nuevo_cliente = cliente.save()
        return nuevo_cliente
    except Exception as error:
        print(f'{error_generico} {error}')

def cliente_por_rut(rut):
    try:
        cliente = Cliente.select().where(Cliente.rut_cliente == rut)
        if cliente:
            return cliente
    except Exception as error:
        print(f'{error_generico} {error}')

def cliente_por_id(id):
    try:
        cliente = Cliente[id]
        if cliente:
            return cliente
    except Cliente.DoesNotExist:
        print('Cliente NO encontrado.')
    except Exception as error:
        print(f'{error_generico} {error}')