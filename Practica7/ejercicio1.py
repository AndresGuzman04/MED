class Divisor:
    def dividir(self, numerador, denominador):
        try:
            resultado = numerador / denominador
            return resultado
        except ZeroDivisionError:
            return "Error: No se puede dividir a cero."

divisor = Divisor()
resultado = divisor.dividir(10, 0)
print(resultado)
