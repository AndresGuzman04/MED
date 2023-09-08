miDiccionario = dict()

otroDiccionario = {}

otraFormaDeclaracion = {
    'clave1' : 10,
    1 : True,
    'otraClave' : [1, 2, 3],
    'cadena' : 'Este es unmensaje',
    'diccionario' : miDiccionario
}

print(otraFormaDeclaracion)
print(otraFormaDeclaracion['clave1'])
print(otraFormaDeclaracion[1])
print(otraFormaDeclaracion['otraClave'])
print(otraFormaDeclaracion['cadena'])
print(otraFormaDeclaracion['diccionario'])

# Limpiar
#otraFormaDeclaracion.clear()

copia = otraFormaDeclaracion.copy()

print(copia)

persona = {
    'nombres' : 'Josue Isai',
    'apellidos' : 'Herrera Nenitez'
}

print(persona.get('nombres'))
print(persona.get('apellidos'))

claves = ('nota1', 'nota2', 'nota3')
notas = dict.fromkeys(claves)
print(notas['nota4'])

