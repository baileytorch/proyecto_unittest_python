from prettytable import PrettyTable

from ..negocio import cargar_clientes, crear_cliente, cargar_cliente, modificar_cliente
from ..auxiliares import validar_rut, validar_correo, validar_fecha_nacimiento, error_generico

def listado_clientes():
    print('LISTADO CLIENTES')
    print('================\n')
    try:
        tabla_clientes = PrettyTable()
        tabla_clientes = cargar_clientes(tabla_clientes)
        print(tabla_clientes)
    except Exception as error:
        print(f'{error_generico} {error}')
        
def ingresar_cliente():
    rut = nombre = apellido = correo = fecha_nacimiento = ''

    print('AGREGAR NUEVO CLIENTE')
    print('=====================')
    print('Ingrese Datos de Cliente\n')
    try:
        while rut == '':
            rut = input('RUT (12.345.678-5): ')
            rut, respuesta = validar_rut(rut)
            print(respuesta)

        while nombre == '':
            nombre = input('Nombre: ')

        while apellido == '':
            apellido = input('Apellido: ')

        while correo == '':
            correo = input('Correo: ')
            correo, mensaje = validar_correo(correo)
            print(mensaje)

        while fecha_nacimiento == '':
            fecha_nacimiento = input('Fecha Nacimiento (dd/mm/yyyy): ')
            fecha_nacimiento, mensaje = validar_fecha_nacimiento(fecha_nacimiento)
            print(mensaje)
        
        crear_cliente(rut, nombre.title(), apellido.title(), correo, fecha_nacimiento)
    except Exception as mensaje:
        print(f'{error_generico} {mensaje}')

def actualizar_cliente():
    rut = nombre = apellido = correo = fecha_nacimiento = ''
    tabla_cliente = PrettyTable()
    
    print('MODIFICAR CLIENTE')
    print('=================')
    rut = input('Ingrese RUT cliente a modificar: ')
    tabla_cliente, cliente = cargar_cliente(tabla_cliente, rut)
    print(tabla_cliente)
        
    try:
        while rut == '':
            rut = input('Nuevo RUT (12.345.678-5) (ENTER para mantener): ')
            rut, respuesta = validar_rut(rut)
            print(respuesta)
    
        while nombre == '':
            nombre = input('Nuevo Nombre (ENTER para mantener): ')
    
        while apellido == '':
            apellido = input('Nuevo Apellido (ENTER para mantener): ')
    
        while correo == '':
            correo = input('Nuevo Correo (ENTER para mantener): ')
            correo, mensaje = validar_correo(correo)
            print(mensaje)
    
        while fecha_nacimiento == '':
            fecha_nacimiento = input('Nueva Fecha Nacimiento (dd/mm/yyyy) (ENTER para mantener): ')
            fecha_nacimiento, mensaje = validar_fecha_nacimiento(fecha_nacimiento)
            print(mensaje)
        
        modificar_cliente(cliente, rut, nombre.title(), apellido.title(), correo, fecha_nacimiento)
    except Exception as mensaje:
        print(f'{error_generico} {mensaje}')