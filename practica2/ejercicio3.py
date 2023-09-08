numeros = [1, 4, 6, 7, 8, 10, 13, 2, 9, 28, 9, 10, 7, 3, 8]

numerosPares = []
numerosImpares = []


for numero in numeros:
    if (numero % 2) == 0:
        numerosPares.append(numero)
    else:
            numerosImpares.append(numero)
print("Lista numeros random: ", numeros)
print("Lista numeros pares: ", numerosPares)
print("Lista numeros impares: ", numerosImpares)