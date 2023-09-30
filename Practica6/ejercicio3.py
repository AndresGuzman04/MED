class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def actualizar_carnet(self, nuevo_carnet):
        self.carnet = nuevo_carnet

    def actualizar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCarnet: {self.carnet}\nCarrera: {self.carrera}"


estudiante1 = Estudiante("Juan", "Pérez", "12345", "Ingeniería de Softwaree")


print("Información inicial del estudiante:")
print(estudiante1.obtener_informacion())


estudiante1.actualizar_nombre("María")
estudiante1.actualizar_carnet("54321")


print("\nInformación actualizada del estudiante:")
print(estudiante1.obtener_informacion())
