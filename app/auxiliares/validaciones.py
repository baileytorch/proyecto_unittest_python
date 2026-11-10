import re
from datetime import datetime
from decimal import Decimal, InvalidOperation


def _validar_texto_producto(valor, nombre_campo, maximo=None):
    valor = valor.strip()
    if not valor:
        return None, f"El {nombre_campo} es obligatorio."
    if maximo is not None and len(valor) > maximo:
        return None, f"El {nombre_campo} no puede exceder {maximo} caracteres."
    return valor, f"{nombre_campo.capitalize()} válido."


def validar_sku_producto(sku):
    return _validar_texto_producto(sku, "SKU", 50)


def validar_nombre_producto(nombre):
    return _validar_texto_producto(nombre, "nombre", 255)


def validar_descripcion_producto(descripcion):
    return _validar_texto_producto(descripcion, "descripción")


def validar_precio_producto(valor):
    valor = valor.strip()
    if not valor:
        return None, "El precio es obligatorio."

    try:
        precio = Decimal(valor)
    except InvalidOperation:
        return None, "El precio debe ser numérico."

    if not precio.is_finite():
        return None, "El precio debe ser un número finito."
    if precio < 0:
        return None, "El precio no puede ser negativo."
    if precio.as_tuple().exponent < -2:
        return None, "El precio admite como máximo dos decimales."
    if precio > Decimal("99999999.99"):
        return None, "El precio excede el máximo permitido."
    return precio, "Precio válido."

def validar_rut(rut):
    patron_rut = r'^\d{1,3}(\.?\d{3})*-[0-9kK]$'
    
    if re.match(patron_rut, rut):
        rut_limpio = rut.replace('.', '').replace('-', '')
        dig_ver = rut_limpio[-1]
        num_rut = rut_limpio[:-1]
        rut_invertido = num_rut[::-1]
        
        multiplicador = 2
        suma = 0
        
        for num in rut_invertido:
            suma += int(num) * multiplicador
            multiplicador += 1
            if multiplicador > 7:
                multiplicador = 2
                
        resto = suma % 11
        final = 11 - resto
        
        digito_calculado = ''
        if final == 11:
            digito_calculado = '0'
        elif final == 10:
            digito_calculado = 'k'
        else:
            digito_calculado = str(final)
            
        if digito_calculado.upper() == dig_ver.upper():
            mensaje = 'RUT válido'
        else:
            mensaje = 'RUT inválido'
            rut = ''
    else:
        mensaje = 'Formato de RUT incorrecto'
        rut = ''
    
    return rut, mensaje

def validar_correo(correo):
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(patron_correo, correo):
        mensaje = 'Formato de correo incorrecto'
        correo = ''
    else:
        mensaje = 'Formato de correo correcto'
    
    return correo, mensaje
    
def validar_fecha_nacimiento(fecha_nacimiento):
    patron_fecha = r'^\b(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/(19\d\d|20\d\d)\b$'
    
    if not re.match(patron_fecha, fecha_nacimiento):
        mensaje = 'Formato de fecha NO corresponde, ingrese nuevamente...'
        fecha_nacimiento = ''
    else:
        try:
            mensaje = 'Formato de fecha correcto.'
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            mensaje = 'Fecha INVÁLIDA, ingrese nuevamente...'
            fecha_nacimiento = ''
            
    return fecha_nacimiento, mensaje