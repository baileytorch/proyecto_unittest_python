
import unittest
from app.modelos.cliente import Cliente

class TestCliente(unittest.TestCase):

    def test_creacion_cliente(self):

        cliente = Cliente(
            1,
            "Juan Perez",
            "12.345.678-5",
            "juan@gmail.com",
            "1990-10-10",
            "987654321"
        )

        self.assertEqual(cliente.nombre, "Juan Perez")
        self.assertNotEqual(cliente.nombre,"Hola")
        self.assertEqual(cliente.email, "juan@gmail.com")
        self.assertEqual(cliente.telefono, "987654321")

if __name__ == "__main__":
    unittest.main()
