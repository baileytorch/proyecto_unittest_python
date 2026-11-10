from peewee import (
    SQL,
    Model,
    AutoField,
    BooleanField,
    ForeignKeyField,
    IntegerField,
    DecimalField,
)

from ..datos.conexion import database
from .pedido import Pedido
from .producto import Producto

class BaseModel(Model):
    class Meta:
        database = database
        
class DetallePedido(BaseModel):
    id_detalle_pedido = AutoField()
    id_pedido = ForeignKeyField(Pedido, backref="detalles", column_name="id_pedido")
    id_producto = ForeignKeyField(Producto, backref="detalles", column_name="id_producto")
    cantidad = IntegerField(default=1)
    precio_unitario = DecimalField(max_digits=10, decimal_places=2, default=0.00)
    habilitado = BooleanField(constraints=[SQL(True)])

    class Meta:
        table_name = "detalle_pedidos"

    def __str__(self):
        return f"Pedido: {self.id_pedido} - Producto: {self.id_producto}"