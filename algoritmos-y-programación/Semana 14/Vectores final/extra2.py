# Ejercicio 2 | Vectores final | Jesús Domínguez

"""
Este un algoritmo que convierte una lista de números
que el usuario escriba a frase, donde cada número representa 
la ubicación o el índice de cada caracter en la lista abecedario.
Solo funciona con minúsculas y algunos caracteres especiales.

Esta idea surguió mientras hacía el segundo
ejercicio de práctica de vectores o listas.
"""

# Definir lista abecedario:
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "-", " ", ".", ",", ";", ":", "¿", "?", "á", "é", "í", "ó", "ú", "ä", "ë", "ï", "ö", "ü"]

# Capturar mensaje incriptado:
mensaje_incriptado = []
cantidad_elementos = eval(input("Ingrese la cantidad de elementos del mensaje incriptado: "))

i = 0
while i < cantidad_elementos:
    elemento = eval(input(f"Ingrese el elemento mensaje_incriptado[{i}]: "))
    mensaje_incriptado.append(elemento)
    i = i + 1

# Desincriptar mensaje:
mensaje_desincriptado = ""
i = 0
while i < cantidad_elementos:
    caracter = abecedario[mensaje_incriptado[i]]
    mensaje_desincriptado = mensaje_desincriptado + caracter
    i = i + 1

# Resultados:
print("- - RESULTADOS - -")
print("Mensaje incriptado:", mensaje_incriptado)
print("Mensaje desincriptado:", mensaje_desincriptado)