notas = []

for i in range(5):
    nota = float(input(f"Ingrese la nota {i + 1} (entre 0 y 10): "))
    while nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10.")
        nota = float(input(f"Ingrese la nota {i + 1} (entre 0 y 10): "))

    notas.append(nota)


print("Notas obtenidas:")
print(notas)
    
media = sum(notas) / len(notas)

nota_maxima = max(notas)
nota_minima = min(notas)

print(f"Nota media: {media:.2f}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")