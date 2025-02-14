from clientes.registro import registrar_cliente, clientes
from clientes.login import login_cliente

def mostrar_clientes():
    if clientes:
        print("Clientes Registrados")
        for cliente in clientes.values():
            print(cliente)
    else:
        print("No hay clientes registrados.\n")

def main():
    while True:
        print(" Menú ")
        print("1. Registrar un nuevo cliente")
        print("2. Mostrar clientes registrados")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            login_cliente()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()
