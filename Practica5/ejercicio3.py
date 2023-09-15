
def division(dividendo, divisor):
    if divisor == 0:
        return "La división entre cero no está definida"
    else:
        resultado = dividendo / divisor
        return resultado

dividendo = float(input("Ingresa el dividendo: "))
divisor = float(input("Ingresa el divisor: "))

resultado = division(dividendo, divisor)

print(resultado)