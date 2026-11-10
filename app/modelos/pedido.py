from peewee import SQL,Model, AutoField, BooleanField, ForeignKeyField, DateTimeField, DecimalField
from peewee_enum_field import EnumField

from datetime import datetime
from enum import Enum

from ..datos.conexion import database
from .cliente import Cliente

class BaseModel(Model):
    class Meta:
        database = database

class EstadoPedido(Enum):
    PEND = 'pendiente'
    PROC = 'procesando'
    ENV = 'enviado'
    ENT = 'entregado'
    CANC = 'cancelado'
        
class Pedido(BaseModel):
    id_pedido = AutoField()
    cliente_pedido = ForeignKeyField(
        Cliente,
        backref="pedidos",
        column_name="cliente_pedido",
    )
    fecha_pedido = DateTimeField(null=False, default=datetime.now())
    total_pedido = DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado_pedido = EnumField(EstadoPedido, default=EstadoPedido.PEND)
    pedido_habilitado = BooleanField(constraints=[SQL(True)])

    class Meta:
        table_name = 'pedidos'

    def __str__(self):
        return f"Pedido {self.id_pedido} - Total: ${self.total_pedido}"