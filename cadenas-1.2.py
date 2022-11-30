# Cadenas 1.2 | Jesús Alberto Domínguez Charris

"""
Secuencial
cadena:
    longitud
    vector
    palabras

    invertida
    vocales SIN REPETIR + TILDES
    consonantes SIN REPETIR
    números SIN REPETIR

    signos de puntuación SIN REPETIR
    otros caracteres SIN REPETIR
"""

print("CADENAS 1.2")
cadena = input("Ingrese su cadena: ")

# 1. Longitud
longitud = len(cadena)

# 2. Vector caracteres
vector = []
for x in cadena:
    vector.append(x)

# 3. Lista palabras
palabras = cadena.split()

# 4. Invertir
invertir = cadena[::-1]

# 5. Vocales
vocales = ["a", "e", "i", "o", "u",
           "á", "é", "í", "ó", "ú",
           "à", "è", "ì", "ò", "ù",
           "ä", "ë", "ï", "ö", "ü"]
vocales_cadena = []
for x in cadena:
    if x.lower() in vocales and x not in vocales_cadena:
        vocales_cadena.append(x)

# 6. Consonantes
consonantes = ["b", "c", "d", "f",
               "g", "h", "j", "k",
               "l", "m", "n", "ñ",
               "p", "q", "r", "s",
               "t", "v", "w", "x",
               "y", "z"]
consonantes_cadena = []
for x in cadena:
    if x.lower() in consonantes and x not in consonantes_cadena:
        consonantes_cadena.append(x)

# 7. Números
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numeros_cadena = []
for x in cadena:
    if x in numeros and x not in numeros_cadena:
        numeros_cadena.append(x)

# 8. Signos de puntuación
puntuacion = ["¿", "?", "¡", "!",
              "(", ")", "[", "]",
              "{", "}", ".", ":",
              ",", ";"]
puntuacion_cadena = []
for x in cadena:
    if x.lower() in puntuacion and x not in puntuacion_cadena:
        puntuacion_cadena.append(x)

# 9. Otros caracteres
otros = ["+", "-", "*", "/", "%",
         "<", ">", "=", "|", "°",
         "¬", "#", "$", "&", "\\",
         "¨", "´", "~", "^", "`",
         "_", "@"]
otros_cadena = []
for x in cadena:
    if x.lower() in otros and x not in otros_cadena:
        otros_cadena.append(x)

# Imprimir resultados
print(f"0. Cadena: {cadena}")
print(f"1. Longitud: {longitud}")
print(f"2. Vector: {vector}")
print(f"3. Palabras: {palabras}")
print(f"4. Invertir: {invertir}")
print(f"5. Vocales: {vocales_cadena}")
print(f"6. Consonantes: {consonantes_cadena}")
print(f"7. Números: {numeros_cadena}")
print(f"8. Signos de puntuación: {puntuacion_cadena}")
print(f"9. Otros caracteres: {otros_cadena}")
