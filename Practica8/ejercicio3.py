archivo_nombre = "archivo_inexistente.txt"

try:
    with open(archivo_nombre, "r") as archivo:
        print(f"El archivo {archivo_nombre} se ha abierto exitosamente.")
except FileNotFoundError:
    print(f"El archivo '{archivo_nombre}' no se encuentra.")
except Exception as e:
    print(f"Se produjo un error: {e}")


