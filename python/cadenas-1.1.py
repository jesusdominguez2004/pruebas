# Cadenas 1.1 | Jesús Alberto Domínguez Charris

"""
Secuencial
cadena:
    longitud
    vector
    palabras
    invertida
    vocales
    consonantes
    números
"""

print("CADENAS 1.1")
cadena = input("Ingrese su cadena: ")

# Longitud
longitud = len(cadena)

# Vector caracteres
vector = []
for x in cadena:
    vector.append(x)

# Lista palabras
palabras = cadena.split()

# Invertir
invertir = cadena[::-1]

# Vocales
vocales = ["a", "e", "i", "o", "u"]
vocales_cadena = []
for x in cadena:
    if x.lower() in vocales:
        vocales_cadena.append(x)

# Consonantes
consonantes = ["b", "c", "d", "f",
               "g", "h", "j", "k",
               "l", "m", "n", "ñ",
               "p", "q", "r", "s",
               "t", "v", "w", "x",
               "y", "z"]
consonantes_cadena = []
for x in cadena:
    if x.lower() in consonantes:
        consonantes_cadena.append(x)

# Números
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numeros_cadena = []
for x in cadena:
    if x in numeros:
        numeros_cadena.append(x)

# Resultados
print(f"Cadena: {cadena}")
print(f"Longitud: {longitud}")
print(f"Vector: {vector}")
print(f"Palabras: {palabras}")
print(f"Invertir: {invertir}")
print(f"Vocales: {vocales_cadena}")
print(f"Consonantes: {consonantes_cadena}")
print(f"Números: {numeros_cadena}")
