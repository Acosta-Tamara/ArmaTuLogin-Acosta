class Cliente:
    def __init__(self, nombre_usuario, correo, contrasena, direccion):
        self.nombre_usuario = nombre_usuario
        self.correo = correo
        self.contrasena = contrasena
        self.direccion = direccion

    def __str__(self):
        return f"Cliente: {self.nombre_usuario}, Correo electronico: {self.correo}, Dirección: {self.direccion}"

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"Dirección actualizada a: {self.direccion}")

    def mostrar_info(self):
        print(f"Nombre de usuario: {self.nombre_usuario}")
        print(f"Correo electronico: {self.correo}")
        print(f"Dirección: {self.direccion}")
