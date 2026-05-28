
from modelos.cliente import Cliente
from datos.cliente_repository import ClienteRepository
from negocio.validaciones import validar_email, validar_rut

class ClienteService:

    def __init__(self):
        self.repository = ClienteRepository()

    def crear_cliente(self, id_cliente, nombre, rut, email, fecha_nacimiento, telefono):

        if not validar_email(email):
            raise ValueError("Email inválido")

        if not validar_rut(rut):
            raise ValueError("RUT inválido")

        cliente = Cliente(
            id_cliente,
            nombre,
            rut,
            email,
            fecha_nacimiento,
            telefono
        )

        self.repository.agregar(cliente)

    def obtener_clientes(self):
        return self.repository.listar()
