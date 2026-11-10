
import unittest
from decimal import Decimal

from app.auxiliares import (
    validar_nombre_producto,
    validar_precio_producto,
    validar_rut,
    validar_sku_producto,
)

class TestValidaciones(unittest.TestCase):

    def test_rut_valido(self):
        rut, mensaje = validar_rut("12.345.678-5")
        self.assertEqual(rut, "12.345.678-5")
        self.assertEqual(mensaje, "RUT válido")

    def test_rut_invalido(self):
        rut, mensaje = validar_rut("11.111.111-9")
        self.assertEqual(rut, "")
        self.assertEqual(mensaje, "RUT inválido")

    def test_sku_producto_obligatorio_y_maximo(self):
        self.assertIsNone(validar_sku_producto(" ")[0])
        self.assertIsNone(validar_sku_producto("S" * 51)[0])
        self.assertEqual(validar_sku_producto(" SKU-1 ")[0], "SKU-1")

    def test_nombre_producto_obligatorio_y_maximo(self):
        self.assertIsNone(validar_nombre_producto(" ")[0])
        self.assertIsNone(validar_nombre_producto("N" * 256)[0])
        self.assertEqual(validar_nombre_producto(" Teclado ")[0], "Teclado")

    def test_precio_producto_debe_ser_decimal_valido(self):
        self.assertEqual(validar_precio_producto("12.50")[0], Decimal("12.50"))
        for precio in ("", "-1", "1.234", "NaN", "100000000", "texto"):
            with self.subTest(precio=precio):
                self.assertIsNone(validar_precio_producto(precio)[0])

if __name__ == "__main__":
    unittest.main()
