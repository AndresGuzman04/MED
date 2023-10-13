
nombres = []

while True:
    nombre = input("Ingresa un nombre (o presiona Enter para finalizar): ")
    if nombre:
        nombres.append(nombre)
    else:
        break


with open("nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")
print("Nombres escritos en 'nombres.txt'.")

with open("nombres.txt", "r") as archivo:
    for linea in archivo:
        print(linea, end='')