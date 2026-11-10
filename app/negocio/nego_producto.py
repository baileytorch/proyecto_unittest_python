from prettytable import PrettyTable

from ..datos.repo_producto import listado_productos_habilitados, guardar_producto
from ..modelos.producto import Producto


def cargar_productos(tabla: PrettyTable):
    productos = listado_productos_habilitados()
    tabla.field_names = ["Id", "SKU", "Nombre", "Descripción", "Precio"]

    for producto in productos:
        tabla.add_row([
            producto.id_producto,
            producto.sku_producto,
            producto.nombre_producto,
            producto.descripcion_producto,
            producto.precio_producto,
        ])

    return tabla


def crear_producto(str_sku, str_nombre, str_descripcion, precio):
    nuevo_producto = Producto()
    nuevo_producto.sku_producto = str_sku
    nuevo_producto.nombre_producto = str_nombre
    nuevo_producto.descripcion_producto = str_descripcion
    nuevo_producto.precio_producto = precio
    nuevo_producto.producto_habilitado = True

    respuesta = guardar_producto(nuevo_producto)
    if respuesta:
        print(f"Producto {nuevo_producto.nombre_producto} guardado con éxito.")


def modificar_producto(producto: Producto, str_sku, str_nombre, str_descripcion, precio):
    if producto.sku_producto != str_sku:
        producto.sku_producto = str_sku
    if producto.nombre_producto != str_nombre:
        producto.nombre_producto = str_nombre
    if producto.descripcion_producto != str_descripcion:
        producto.descripcion_producto = str_descripcion
    if producto.precio_producto != precio:
        producto.precio_producto = precio

    respuesta = guardar_producto(producto)
    if respuesta:
        print(f"Producto {producto.nombre_producto} modificado con éxito.")
