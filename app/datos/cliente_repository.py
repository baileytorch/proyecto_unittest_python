
class ClienteRepository:

    def __init__(self):
        self.clientes = []

    def agregar(self, cliente):
        self.clientes.append(cliente)

    def listar(self):
        return self.clientes
