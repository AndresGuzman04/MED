
def ingresar_datos(n):
    datos = []
    for i in range(n):
        dato = float(input(f"Ingrese el dato {i + 1}: "))
        datos.append(dato)
    return datos


def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def sumatoria(lista):
    suma = 0
    for dato in lista:
        suma += dato
    return suma

def calcular_media(lista):
    suma = sumatoria(lista)
    n = len(lista)
    return suma / n

def calcular_mediana(lista):
    lista_ordenada = ordenar_lista(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        mediana = lista_ordenada[n // 2]
    return mediana

def calcular_moda(lista):
    frecuencias = {}
    for dato in lista:
        if dato in frecuencias:
            frecuencias[dato] += 1
        else:
            frecuencias[dato] = 1

    moda = []
    max_frecuencia = max(frecuencias.values())

    for dato, frecuencia in frecuencias.items():
        if frecuencia == max_frecuencia:
            moda.append(dato)

    return moda


def calcular_desviacion_estandar(lista):
    media = calcular_media(lista)
    n = len(lista)
    suma_cuadrados = 0

    for dato in lista:
        suma_cuadrados += (dato - media) ** 2

    desviacion_estandar = (suma_cuadrados / (n - 1)) ** 0.5
    return desviacion_estandar



n = int(input("Ingrese la cantidad de datos a ingresar: "))
datos = ingresar_datos(n)
print("Datos ingresados:", datos)
print("Datos ordenados de menor a mayor:", ordenar_lista(datos))
print("Sumatoria de los datos:", sumatoria(datos))
print("Media de los datos:", calcular_media(datos))
print("Mediana de los datos:", calcular_mediana(datos))
print("Moda de los datos:", calcular_moda(datos))
print("Desviación estándar de los datos:", calcular_desviacion_estandar(datos))

