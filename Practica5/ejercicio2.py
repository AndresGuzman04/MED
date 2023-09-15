def calcular_raiz(numero, n):
    if numero >= 0:
        return pow(numero, 1/n)
    else:
        return "No se puede calcular la raíz de un número negativo."


numero = float(input("Ingresa un número: "))
n = int(input("Ingresa el valor de n para la raíz: "))


resultado = calcular_raiz(numero, n)


print(f"La raíz {n}-ésima de {numero} es: {resultado}")