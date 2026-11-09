import re

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
            return True, 'RUT válido'
        else:
            return False, 'RUT inválido'
    else:
        return False, 'Formato de RUT incorrecto'

def validar_correo(correo):
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron_correo, correo):
        return False, 'Formato de correo incorrecto'
    else:
        return True, 'Formato de correo correcto'

def validar_contrasenia_segura(contrasenia):    
    errores = []

    if len(contrasenia) < 8 or len(contrasenia) > 15:
        errores.append("La contraseña debe tener entre 8 y 15 caracteres.")

    if not any(c.isupper() for c in contrasenia):
        errores.append("La contraseña debe contener al menos una letra mayúscula.")

    if not any(c.islower() for c in contrasenia):
        errores.append("La contraseña debe contener al menos una letra minúscula.")

    if not any(c.isdigit() for c in contrasenia):
        errores.append("La contraseña debe contener al menos un número.")

    if not any(c in "!@#$%&/" for c in contrasenia):
        errores.append("La contraseña debe contener al menos uno de los siguientes caracteres especiales: !, @, #, $, %, &. /.")

    if errores:
        return False, errores
    else:
        return True, ["La contraseña es segura y cumple con todos los requisitos."]
    
def validar_genero(genero):
    if genero not in ['1','2','3']:
        return False, 'Género correcto.'
    else:
        return True, 'Género incorrecto.'