class CuentaUsuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.sesion_iniciada = False

    def iniciar_sesion(self, nombre_usuario, contraseña):
        if nombre_usuario == self.nombre_usuario and contraseña == self.contraseña:
            self.sesion_iniciada = True
            print("Sesión iniciada correctamente.")
        else:
            print("Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo.")

    def cerrar_sesion(self):
        if self.sesion_iniciada:
            self.sesion_iniciada = False
            print("Sesión cerrada correctamente.")
        else:
            print("No hay ninguna sesión activa.")

    def esta_sesion_iniciada(self):
        return self.sesion_iniciada

cuenta = CuentaUsuario("usuario123", "contraseña123")

cuenta.iniciar_sesion("usuario123", "contraseña123")

if cuenta.esta_sesion_iniciada():
    print("El usuario está conectado.")
else:
    print("El usuario no está conectado.")

cuenta.cerrar_sesion()


if cuenta.esta_sesion_iniciada():
    print("El usuario está conectado.")
else:
    print("El usuario no está conectado.")
