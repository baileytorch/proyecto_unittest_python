
from negocio.cliente_service import ClienteService

service = ClienteService()

def iniciar_menu():
    while True:
        print("\n=== SISTEMA DE CLIENTES ===")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")

def agregar_cliente():
    try:
        id_cliente = int(input("ID: "))
        nombre = input("Nombre: ")
        rut = input("RUT: ")
        email = input("Email: ")
        fecha_nacimiento = input("Fecha nacimiento: ")
        telefono = input("Teléfono: ")

        service.crear_cliente(
            id_cliente,
            nombre,
            rut,
            email,
            fecha_nacimiento,
            telefono
        )

        print("Cliente agregado correctamente")

    except Exception as e:
        print(f"Error: {e}")

def listar_clientes():
    clientes = service.obtener_clientes()

    if not clientes:
        print("No existen clientes")
        return

    for cliente in clientes:
        print(cliente)
