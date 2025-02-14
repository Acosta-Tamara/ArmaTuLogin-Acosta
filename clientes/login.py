from clientes.registro import clientes

def login_cliente():
    print(" Login ")
    nombre_usuario = input("Ingresa tu nombre de usuario: ")

    if nombre_usuario in clientes:
        contrasena = input("Ingresa tu contraseña: ")
        if clientes[nombre_usuario].contrasena == contrasena:
            print(f"Bienvenido {nombre_usuario}!\n")
            clientes[nombre_usuario].mostrar_info()
        else:
            print("Contraseña incorrecta.\n")
    else:
        print("Usuario no encontrado.\n")
