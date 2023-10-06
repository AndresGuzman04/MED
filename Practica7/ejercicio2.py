class ValidadorDeEdad:
    def validar(self, edad):
        try:
            edad = int(edad)
            if edad >= 0:
                return f"La edad {edad} es válida."
            else:
                return "Error: La edad no puede ser un número negativo."
        except ValueError:
            return "Error: La edad ingresada no es un número entero válido."

validador_edad = ValidadorDeEdad()
resultado = validador_edad.validar("25")
print(resultado)
