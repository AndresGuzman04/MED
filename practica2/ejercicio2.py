frase = input("Escriba una frase:")

frase = frase.lower() 

conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
for caracter in frase:
    if caracter in conteo_vocales:
        conteo_vocales[caracter] += 1


for vocal, cantidad in conteo_vocales.items():
    print(f"La vocal '{vocal}' aparece {cantidad} veces.")






