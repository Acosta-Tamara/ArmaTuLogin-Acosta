from clientes.cliente import Cliente

clientes = {}

def registrar_cliente():
    print("Registro de Cliente")
    nombre_usuario = input("Introduce el nombre de usuario: ")
    while nombre_usuario in clientes:
        print("El nombre de usuario ya está registrado. Intenta con otro nuevamente.")
        nombre_usuario = input("Introduce el nombre de usuario: ")

    correo = input("Ingresa el correo electronico: ")
    contrasena = input("Ingresa la contraseña: ")
    direccion = input("Ingresa la dirección: ")

    cliente = Cliente(nombre_usuario, correo, contrasena, direccion)
    clientes[nombre_usuario] = cliente
    print(f"Cliente {nombre_usuario} registrado exitosamente.\n")
