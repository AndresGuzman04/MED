numeros = []

i = 1

while i <= 5:
  numeros.append(input("Ingrese un numero:"))
  i = i + 1

print(numeros)

for k in range(4):
    for x in range(4):
        if numeros[x]>numeros[x+1]:
            aux=numeros[x]
            numeros[x]=numeros[x+1]
            numeros[x+1]=aux

print(numeros)