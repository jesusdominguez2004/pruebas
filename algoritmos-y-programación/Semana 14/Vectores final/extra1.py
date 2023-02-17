# Extra | Vectores final | Jesús Domínguez

"""
Este un algoritmo que convierte una frase
que el usuario escriba a una lista de números, 
donde cada número representa la ubicación o el índice
de cada caracter en la lista abecedario. Solo funciona
con minúsculas y algunos caracteres especiales.

Esta idea surguió mientras hacía el segundo
ejercicio de práctica de vectores o listas.
"""

# Definir lista abecedario:
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "-", " ", ".", ",", ";", ":", "¿", "?", "á", "é", "í", "ó", "ú", "ä", "ë", "ï", "ö", "ü"]

# Capturar texto:
mi_texto = input("Ingrese un frase: ")

# Lista de caracteres del texto:
caracteres = []
i = 0
while i < len(mi_texto):
    caracteres.append(mi_texto[i])
    i = i + 1

# Convertir lista de caracteres del texto a lista de números de índices:
mensaje = []
i = 0
while i < len(mi_texto):
    indice = abecedario.index(caracteres[i])
    mensaje.append(indice)
    i = i + 1

# Resultado:
print("- - RESULTADOS - -")
print("Mensaje incriptado:", mensaje)