
class Producto:

    def __init__(self, id_producto, nombre, precio, stock):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
