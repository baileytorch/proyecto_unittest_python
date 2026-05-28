
import unittest
from app.negocio.validaciones import validar_email, validar_rut

class TestValidaciones(unittest.TestCase):

    def test_email_valido(self):
        self.assertTrue(validar_email("correo@gmail.com"))

    def test_email_invalido(self):
        self.assertFalse(validar_email("correo.com"))

    def test_rut_valido(self):
        self.assertTrue(validar_rut("12.345.678-5"))

    def test_rut_invalido(self):
        self.assertFalse(validar_rut("11.111.111-9"))

if __name__ == "__main__":
    unittest.main()
