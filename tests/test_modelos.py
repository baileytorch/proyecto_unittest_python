
import unittest
from app.modelos.cliente import Cliente

class TestCliente(unittest.TestCase):

    def test_creacion_cliente(self):

        cliente = Cliente(
            id_cliente=1,
            rut_cliente="12.345.678-5",
            nombre_cliente="Juan",
            apellido_cliente="Perez",
            correo_cliente="juan@gmail.com",
            fecha_nacimiento_cliente="2000-12-25",
        )

        self.assertEqual(cliente.rut_cliente, "12.345.678-5")
        self.assertNotEqual(cliente.rut_cliente,"12.345.678-9")
        self.assertEqual(cliente.nombre_cliente, "Juan")
        self.assertNotEqual(cliente.nombre_cliente,"Hola")
        self.assertEqual(cliente.correo_cliente, "juan@gmail.com")
        self.assertEqual(cliente.fecha_nacimiento_cliente, "2000-12-25")

if __name__ == "__main__":
    unittest.main()
