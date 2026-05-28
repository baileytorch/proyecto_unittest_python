
import re

def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None

def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "")

    if len(rut) < 2:
        return False

    cuerpo = rut[:-1]
    dv = rut[-1].upper()

    try:
        cuerpo = int(cuerpo)
    except:
        return False

    suma = 0
    multiplo = 2

    for digit in reversed(str(cuerpo)):
        suma += int(digit) * multiplo
        multiplo += 1
        if multiplo > 7:
            multiplo = 2

    resto = suma % 11
    dv_calculado = 11 - resto

    if dv_calculado == 11:
        dv_calculado = "0"
    elif dv_calculado == 10:
        dv_calculado = "K"
    else:
        dv_calculado = str(dv_calculado)

    return dv == dv_calculado
