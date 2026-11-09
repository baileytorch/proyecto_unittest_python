from datos.repositorio_cliente import listado_clientes_habilitados,guardar_cliente
from prettytable import PrettyTable
from modelos import Cliente
from datetime import datetime

def cargar_clientes(tabla: PrettyTable):
    clientes = listado_clientes_habilitados()
    tabla.field_names = ['Id','RUT','Nombre Completo','Correo','Fecha Nacimiento','Fecha Incorporación']

    if len(clientes) > 0:
        for cliente in clientes:
            nombre_completo = f'{cliente.nombre_cliente} {cliente.apellido_cliente}'
    
            tabla.add_row([
                cliente.id_cliente, 
                cliente.rut_cliente, 
                nombre_completo, 
                cliente.correo_cliente, 
                cliente.fecha_nacimiento_cliente,
                cliente.fecha_incorporacion_cliente])

    return tabla

def crear_cliente(str_rut, str_nombre, str_apellido, str_correo, str_fecha_nacimiento):
    nuevo_cliente = Cliente()
    nuevo_cliente.rut_cliente = str_rut
    nuevo_cliente.nombre_cliente = str_nombre
    nuevo_cliente.apellido_cliente = str_apellido
    nuevo_cliente.correo_cliente = str_correo
    
    if str_fecha_nacimiento == '':
        nuevo_cliente.fecha_nacimiento = None
    else:        
        nuevo_cliente.fecha_nacimiento = datetime.strptime(str_fecha_nacimiento, "%d/%m/%Y")
    
    nuevo_cliente.fecha_incorporacion = datetime.now()
    nuevo_cliente.habilitado = True

    cliente = guardar_cliente(nuevo_cliente)
    if cliente == 1:
        print(f'Cliente guardado con éxito {nuevo_cliente.nombre} con ID: {nuevo_cliente.id_usuario}')