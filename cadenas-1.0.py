# Cadenas 1.0 | Jesús Alberto Domínguez Charris

"""
Secuencial
cadena:
    longitud
    vector
    palabras
"""

print("CADENAS 1.0")
cadena = input("Ingrese su cadena: ")

longitud = len(cadena)
vector = []
for i in cadena:
    vector.append(i)
palabras = cadena.split()

print(f"Cadena: {cadena}")
print(f"Longitud: {longitud}")
print(f"Vector: {vector}")
print(f"Palabras: {palabras}")
