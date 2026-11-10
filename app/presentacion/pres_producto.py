from prettytable import PrettyTable

from ..datos import producto_por_sku
from ..negocio import cargar_productos, crear_producto, modificar_producto
from ..auxiliares import (
    error_generico,
    validar_descripcion_producto,
    validar_nombre_producto,
    validar_precio_producto,
    validar_sku_producto,
)


def listado_productos():
    print("LISTADO DE PRODUCTOS")
    print("====================")
    try:
        tabla = cargar_productos(PrettyTable())
        print(tabla)
    except Exception as error:
        print(f"{error_generico} {error}")


def ingresar_producto():
    print("AGREGAR PRODUCTO")
    print("================")
    try:
        sku = _solicitar_validado("SKU: ", validar_sku_producto)
        nombre = _solicitar_validado("Nombre: ", validar_nombre_producto)
        descripcion = _solicitar_validado(
            "Descripción: ",
            validar_descripcion_producto,
        )
        precio = _solicitar_validado("Precio: ", validar_precio_producto)

        crear_producto(sku, nombre, descripcion, precio)
    except Exception as error:
        print(f"{error_generico} {error}")


def actualizar_producto():
    print("MODIFICAR PRODUCTO")
    print("==================")
    try:
        sku_actual = input("Ingrese el SKU del producto a modificar: ").strip()
        resultados = producto_por_sku(sku_actual)
        producto = resultados.first() if resultados is not None else None
        if producto is None:
            print("Producto NO encontrado.")
            return

        print(PrettyTable(
            ["SKU", "Nombre", "Descripción", "Precio"],
            [[producto.sku_producto, producto.nombre_producto,
              producto.descripcion_producto, producto.precio_producto]],
        ))

        sku_ingresado = input(
            f"Nuevo SKU (ENTER para mantener {producto.sku_producto}): "
        ).strip()
        sku = (
            _validar_actualizado(sku_ingresado, validar_sku_producto)
            if sku_ingresado
            else producto.sku_producto
        )
        nombre_ingresado = input(
            f"Nuevo nombre (ENTER para mantener {producto.nombre_producto}): "
        ).strip()
        nombre = (
            _validar_actualizado(nombre_ingresado, validar_nombre_producto)
            if nombre_ingresado
            else producto.nombre_producto
        )
        descripcion_ingresada = input(
            "Nueva descripción "
            f"(ENTER para mantener {producto.descripcion_producto}): "
        ).strip()
        descripcion = (
            _validar_actualizado(
                descripcion_ingresada,
                validar_descripcion_producto,
            )
            if descripcion_ingresada
            else producto.descripcion_producto
        )
        precio_ingresado = input(
            f"Nuevo precio (ENTER para mantener {producto.precio_producto}): "
        ).strip()
        precio = (
            _validar_actualizado(precio_ingresado, validar_precio_producto)
            if precio_ingresado
            else producto.precio_producto
        )

        modificar_producto(producto, sku, nombre, descripcion, precio)
    except Exception as error:
        print(f"{error_generico} {error}")


def _solicitar_validado(mensaje, validador):
    while True:
        valor, respuesta = validador(input(mensaje))
        print(respuesta)
        if valor is not None:
            return valor


def _validar_actualizado(valor, validador):
    resultado, respuesta = validador(valor)
    print(respuesta)
    if resultado is None:
        raise ValueError(respuesta)
    return resultado
