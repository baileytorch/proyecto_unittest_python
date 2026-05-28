
class Pedido:

    def __init__(self, id_pedido, cliente_id, fecha, total):
        self.id = id_pedido
        self.cliente_id = cliente_id
        self.fecha = fecha
        self.total = total

    def __str__(self):
        return f"Pedido {self.id} - Total: ${self.total}"
