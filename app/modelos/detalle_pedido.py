from peewee import SQL,Model, AutoField, BooleanField, ForeignKeyField, DateTimeField

from datetime import datetime

from datos.conexion import conectar
from modelos.cliente import Cliente

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos
        
class DetallePedido(BaseModel):
    id_detalle_pedido = AutoField()
    id_pedido = ForeignKeyField(Cliente, backref='pedidos')
    id_producto = DateTimeField(null=False, default=datetime.now())
    habilitado = BooleanField(constraints=[SQL(True)])

    class Meta:
        table_name = 'pedidos'

    def __str__(self):
        return f"Pedido: {self.id_pedido} - Producto: {self.id_producto}"