from datos import base_datos
from modelos import Producto

database = base_datos()

def listado_productos_habilitados():
    try:
        productos = Producto.select().where(Producto.producto_habilitado == True)
        return productos
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def listado_productos_deshabilitados():
    try:
        productos = Producto.select().where(Producto.producto_habilitado == False)
        return productos
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def listado_productos():
    try:
        productos = Producto.select()
        return productos
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def guardar_producto(producto: Producto):
    try:
        nuevo_producto = producto.save()
        return nuevo_producto
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def producto_por_sku(sku):
    try:
        producto = Producto.select().where(Producto.sku_producto == sku)
        return producto
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def producto_por_id(id):
    try:
        producto = Producto[id]
        if producto:
            return producto
    except Producto.DoesNotExist:
        print('El producto indicado NO existe.')
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')