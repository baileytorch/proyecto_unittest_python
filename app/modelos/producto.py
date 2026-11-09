from peewee import SQL,Model, AutoField, BooleanField, CharField, TextField, DecimalField

from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos
        
class Producto(BaseModel):
    id_producto = AutoField()
    sku_producto = CharField(max_length=50,null=False)
    nombre_producto = CharField(null=True)
    descripcion_producto = TextField(max_length=25,null=False)
    precio_producto = DecimalField(max_digits=10, decimal_places=2, default=0.00)
    producto_habilitado = BooleanField(constraints=[SQL(True)])

    class Meta:
        table_name = 'productos'

    def __str__(self):
        return f"{self.nombre_producto} - ${self.precio}"
