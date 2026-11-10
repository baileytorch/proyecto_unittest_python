from ..datos.repo_cliente import listado_clientes_habilitados, guardar_cliente, cliente_por_rut
from prettytable import PrettyTable
from ..modelos.cliente import Cliente
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

def cargar_cliente(tabla: PrettyTable, rut):
    tabla.field_names = ['Id','RUT','Nombre Completo','Correo','Fecha Nacimiento','Fecha Incorporación','Estado']
    cliente = cliente_por_rut(rut)

    if cliente:
        nombre_completo = f'{cliente.nombre_cliente} {cliente.apellido_cliente}'
        habilitado = 'Habilitado' if cliente.cliente_habilitado else 'Deshabilitado'
        tabla.add_row([
            cliente.id_cliente, 
            cliente.rut_cliente, 
            nombre_completo, 
            cliente.correo_cliente, 
            cliente.fecha_nacimiento_cliente,
            cliente.fecha_incorporacion_cliente,
            habilitado])

    return tabla, cliente

def crear_cliente(str_rut, str_nombre, str_apellido, str_correo, str_fecha_nacimiento):
    nuevo_cliente = Cliente()
    nuevo_cliente.rut_cliente = str_rut
    nuevo_cliente.nombre_cliente = str_nombre
    nuevo_cliente.apellido_cliente = str_apellido
    nuevo_cliente.correo_cliente = str_correo
    nuevo_cliente.fecha_nacimiento_cliente = datetime.strptime(str_fecha_nacimiento, "%d/%m/%Y")    
    nuevo_cliente.fecha_incorporacion_cliente = datetime.now()
    nuevo_cliente.cliente_habilitado = True

    respuesta = guardar_cliente(nuevo_cliente)
    if respuesta == 1:
        print(f'Cliente {nuevo_cliente.apellido_cliente}, {nuevo_cliente.nombre_cliente} guardado con éxito.')

def modificar_cliente(cliente: Cliente, str_rut, str_nombre, str_apellido, str_correo, str_fecha_nacimiento):    
    if cliente.rut_cliente != str_rut:
        cliente.rut_cliente = str_rut
    if cliente.nombre_cliente != str_nombre:
        cliente.nombre_cliente = str_nombre
    if cliente.apellido_cliente != str_apellido:
        cliente.apellido_cliente = str_apellido
    if cliente.correo_cliente != str_correo:
        cliente.correo_cliente = str_correo
    if str_fecha_nacimiento:
        fecha_nacimiento = (
            str_fecha_nacimiento
            if isinstance(str_fecha_nacimiento, datetime)
            else datetime.strptime(str_fecha_nacimiento, "%d/%m/%Y")
        )
        if cliente.fecha_nacimiento_cliente != fecha_nacimiento.date():
            cliente.fecha_nacimiento_cliente = fecha_nacimiento.date()

    respuesta = guardar_cliente(cliente)
    if respuesta == 1:
        print(f'Cliente {cliente.apellido_cliente}, {cliente.nombre_cliente} modificado con éxito.')