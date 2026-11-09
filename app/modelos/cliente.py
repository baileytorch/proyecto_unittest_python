from peewee import SQL,Model, AutoField, BooleanField, DateField, CharField, DateTimeField

from datetime import datetime

from datos.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos
        
class Cliente(BaseModel):
    id_cliente = AutoField()
    rut_cliente = CharField(max_length=12,null=False,unique=True)
    nombre_cliente = CharField(max_length=25,null=False)
    apellido_cliente = CharField(max_length=25,null=False)
    correo_cliente = CharField(max_length=255,null=False,unique=True)
    fecha_nacimiento_cliente = DateField(null=True)
    fecha_incorporacion_cliente = DateTimeField(null=False, default=datetime.now())
    cliente_habilitado = BooleanField(constraints=[SQL(True)])

    class Meta:
        table_name = 'clientes'

    def __str__(self):
        return f"{self.apellido_cliente}, {self.nombre_cliente}"
