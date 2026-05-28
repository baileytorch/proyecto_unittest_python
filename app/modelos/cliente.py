
class Cliente:

    def __init__(self, id_cliente, nombre, rut, email, fecha_nacimiento, telefono):
        self.id = id_cliente
        self.nombre = nombre
        self.rut = rut
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.email}"
