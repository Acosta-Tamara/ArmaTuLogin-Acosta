
usuarios = {}

# Registrar un nuevo usuario
def registrar_usuario():
    print("----- Registro de usuario -----")
    nombre_usuario = input("Introduce el nombre de usuario: ")
    while nombre_usuario in usuarios:
        print("El nombre de usuario ya está registrado. Intenta con otro.")
        nombre_usuario = input("Introduce el nombre de usuario: ")
    
    contrasena = input("Introduce la contraseña: ")
    usuarios[nombre_usuario] = contrasena
    print(f"Usuario {nombre_usuario} registrado exitosamente.\n")

# Mostrar todos los usuarios registrados (opcional)
def mostrar_usuarios():
    if usuarios:
        print("----- Usuarios registrados -----")
        for usuario in usuarios:
            print(f"Nombre de usuario: {usuario}")
    else:
        print("No hay usuarios registrados.\n")

#Login
def login_usuario():
    print("----- Login -----")
    nombre_usuario = input("Introduce tu nombre de usuario: ")
    
    if nombre_usuario in usuarios:
        contrasena = input("Introduce tu contraseña: ")
        if usuarios[nombre_usuario] == contrasena:
            print(f"Bienvenido {nombre_usuario}!\n")
        else:
            print("Contraseña incorrecta.\n")
    else:
        print("Usuario no encontrado.\n")

# Flujo del programa
def main():
    while True:
        print("----- Menú -----")
        print("1. Registrar un nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Iniciar sesión")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            login_usuario()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.\n")

# Ejecución final
if __name__ == "__main__":
    main()
