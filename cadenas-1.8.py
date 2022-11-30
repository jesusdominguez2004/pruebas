# Cadenas 1.8 | Jesús Alberto Domínguez Charris

"""
Secuencial
cadena:
    invertida
    longitud
    vector
    palabras

    vocales SIN REPETIR + TILDES
    consonantes SIN REPETIR
    números SIN REPETIR
    signos de puntuación SIN REPETIR
    otros caracteres SIN REPETIR

    palabras CANTIDAD
    vocales CANTIDAD
    consonantes CANTIDAD
    números CANTIDAD
    signos de puntuación CANTIDAD
    otros caracteres CANTIDAD
    mayúsculas CANTIDAD
    minúsculas CANTIDAD
    espacios CANTIDAD

menú
guardar en txt
leer txt
funciones
time sleep
guardar json
"""
from time import sleep
import json

cadena = ""
invertir = ""
vector = []
longitud = 0
palabras = []
cantidad_palabras = 0
cantidad_vocales = 0
vocales = []
vocales_cadena = []
cantidad_consonantes = 0
consonantes = []
consonantes_cadena = []
cantidad_numeros = 0
numeros = []
numeros_cadena = []
cantidad_puntuacion = 0
puntuacion = []
puntuacion_cadena = []
cantidad_otros = 0
otros = []
otros_cadena = []
cantidad_mayusculas = 0
cantidad_minusculas = 0
cantidad_espacios = 0
diccionario = {}


def leer_cadena():
    global cadena
    global invertir
    global vector
    global longitud
    global palabras
    global cantidad_palabras
    global cantidad_vocales
    global vocales
    global vocales_cadena
    global cantidad_consonantes
    global consonantes
    global consonantes_cadena
    global cantidad_numeros
    global numeros
    global numeros_cadena
    global cantidad_puntuacion
    global puntuacion
    global puntuacion_cadena
    global cantidad_otros
    global otros
    global otros_cadena
    global cantidad_mayusculas
    global cantidad_minusculas
    global cantidad_espacios

    cadena = input("Ingrese su cadena: ")
    # 1. Invertir
    invertir = cadena[::-1]
    # 2. Longitud
    longitud = len(cadena)
    # 3. Vector caracteres
    vector = []
    for x in cadena:
        vector.append(x)
    # 4. Lista palabras
    palabras = cadena.split()
    cantidad_palabras = len(palabras)
    # 5. Vocales
    cantidad_vocales = 0
    vocales = ["a", "e", "i", "o", "u",
               "á", "é", "í", "ó", "ú",
               "à", "è", "ì", "ò", "ù",
               "ä", "ë", "ï", "ö", "ü"]
    vocales_cadena = []
    for x in cadena:
        if x.lower() in vocales:
            cantidad_vocales += 1
            if x not in vocales_cadena:
                vocales_cadena.append(x)
    # 6. Consonantes
    cantidad_consonantes = 0
    consonantes = ["b", "c", "d", "f",
                   "g", "h", "j", "k",
                   "l", "m", "n", "ñ",
                   "p", "q", "r", "s",
                   "t", "v", "w", "x",
                   "y", "z"]
    consonantes_cadena = []
    for x in cadena:
        if x.lower() in consonantes:
            cantidad_consonantes += 1
            if x not in consonantes_cadena:
                consonantes_cadena.append(x)
    # 7. Números
    cantidad_numeros = 0
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numeros_cadena = []
    for x in cadena:
        if x in numeros:
            cantidad_numeros += 1
            if x not in numeros_cadena:
                numeros_cadena.append(x)
    # 8. Signos de puntuación
    cantidad_puntuacion = 0
    puntuacion = ["¿", "?", "¡", "!",
                  "(", ")", "[", "]",
                  "{", "}", ".", ":",
                  ",", ";"]
    puntuacion_cadena = []
    for x in cadena:
        if x.lower() in puntuacion:
            cantidad_puntuacion += 1
            if x not in puntuacion_cadena:
                puntuacion_cadena.append(x)
    # 9. Otros caracteres
    cantidad_otros = 0
    otros = ["+", "-", "*", "/", "%",
             "<", ">", "=", "|", "°",
             "¬", "#", "$", "&", "\\",
             "¨", "´", "~", "^", "`",
             "_", "@"]
    otros_cadena = []
    for x in cadena:
        if x.lower() in otros:
            cantidad_otros += 1
            if x not in otros_cadena:
                otros_cadena.append(x)
    # 10. Cantidad mayúsculas y minúsculas
    cantidad_mayusculas = 0
    cantidad_minusculas = 0
    for x in cadena:
        if x.isupper():
            cantidad_mayusculas += 1
        if x.islower():
            cantidad_minusculas += 1
    # 11. Cantidad espacios
    cantidad_espacios = 0
    for x in cadena:
        if x.isspace():
            cantidad_espacios += 1


while True:
    print("CADENAS 1.8 | Jesús Alberto Domínguez Charris")
    print("1. Consola\n2. Guardar en txt\n3. Leer txt\n4. Guardar en json\n5. Salir")
    menu = input(">>> ")

    if menu == "1":
        leer_cadena()
        # Imprimir resultados
        print(f"Cadena: {cadena}")
        print(f"1. Invertir: {invertir}")
        print(f"2. Longitud: {longitud}")
        print(f"3. Lista caracteres: {vector}")
        print(f"4. Lista palabras: {palabras}")
        print(f"5. Lista vocales: {vocales_cadena}")
        print(f"6. Lista consonantes: {consonantes_cadena}")
        print(f"7. Lista números: {numeros_cadena}")
        print(f"8. Lista signos de puntuación: {puntuacion_cadena}")
        print(f"9. Lista otros caracteres: {otros_cadena}")
        print(f"10. Cantidad palabras: {cantidad_palabras}")
        print(f"11. Cantidad vocales: {cantidad_vocales}")
        print(f"12. Cantidad consonantes: {cantidad_consonantes}")
        print(f"13. Cantidad números: {cantidad_numeros}")
        print(f"14. Cantidad signos de puntuación: {cantidad_puntuacion}")
        print(f"15. Cantidad otros caracteres: {cantidad_otros}")
        print(f"16. Cantidad mayúsculas: {cantidad_mayusculas}")
        print(f"17. Cantidad minúsculas: {cantidad_minusculas}")
        print(f"18. Cantidad espacios: {cantidad_espacios}\n")

    elif menu == "2":
        leer_cadena()
        # Guardar en un txt
        with open("cadenas-1.8.txt", "w", encoding="utf-8") as file:
            file.write(f"Cadena: {cadena}\n")
            file.write(f"1. Invertir: {invertir}\n")
            file.write(f"2. Longitud: {longitud}\n")
            file.write(f"3. Lista caracteres: {vector}\n")
            file.write(f"4. Lista palabras: {palabras}\n")
            file.write(f"5. Lista vocales: {vocales_cadena}\n")
            file.write(f"6. Lista consonantes: {consonantes_cadena}\n")
            file.write(f"7. Lista números: {numeros_cadena}\n")
            file.write(f"8. Lista signos de puntuación: {puntuacion_cadena}\n")
            file.write(f"9. Lista otros caracteres: {otros_cadena}\n")
            file.write(f"10. Cantidad palabras: {cantidad_palabras}\n")
            file.write(f"11. Cantidad vocales: {cantidad_vocales}\n")
            file.write(f"12. Cantidad consonantes: {cantidad_consonantes}\n")
            file.write(f"13. Cantidad números: {cantidad_numeros}\n")
            file.write(f"14. Cantidad signos de puntuación: {cantidad_puntuacion}\n")
            file.write(f"15. Cantidad otros caracteres: {cantidad_otros}\n")
            file.write(f"16. Cantidad mayúsculas: {cantidad_mayusculas}\n")
            file.write(f"17. Cantidad minúsculas: {cantidad_minusculas}\n")
            file.write(f"18. Cantidad espacios: {cantidad_espacios}")
            print("¡Proceso de guardado txt finalizado!\n")

    elif menu == "3":
        # Leer un txt
        with open("cadenas-1.8.txt", "r", encoding="utf-8") as file:
            contenido = file.read()
            print(contenido)
            print("¡Proceso de lectura txt finalizado!\n")

    elif menu == "4":
        diccionario = {
            "cadena": cadena,
            "invertir": invertir,
            "vector": vector,
            "longitud": longitud,
            "palabras": palabras,
            "cantidad_palabras": cantidad_palabras,
            "cantidad_vocales": cantidad_vocales,
            "vocales_cadena": vocales_cadena,
            "cantidad_consonantes": cantidad_consonantes,
            "consonantes_cadena": consonantes_cadena,
            "cantidad_numeros": cantidad_numeros,
            "numeros_cadena": numeros_cadena,
            "cantidad_puntuacion": cantidad_puntuacion,
            "puntuacion_cadena": puntuacion_cadena,
            "cantidad_otros": cantidad_otros,
            "otros_cadena": otros_cadena,
            "cantidad_mayusculas": cantidad_mayusculas,
            "cantidad_minusculas": cantidad_minusculas,
            "cantidad_espacios": cantidad_espacios
        }
        print(type(diccionario), diccionario)
        print(type(json.dumps(diccionario)), json.dumps(diccionario))
        with open("json-1.8.txt", "w", encoding="utf-8") as file:
            json.dump(diccionario, file)
        print("¡Proceso de guardado json finalizado!\n")

    elif menu == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Datos incorrectos...")

    # Pausa entre cada proceso
    sleep(1.5)
