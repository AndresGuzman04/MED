
def suma_numeros(*argumentos):
    suma = 0
    for num in argumentos:
        suma += num
    return suma

numeros = []

while True:
    try:
        numero = float(input("Ingresa un número o  enter para cerrar: "))
        numeros.append(numero)
    except ValueError:
        break
    
resultado = suma_numeros(*numeros)

print("La suma es:", resultado)
