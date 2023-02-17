# Listas de elementos

# 1. Lista de elementos a un archivo binario FORMA 1
lista = ["manzana\n", "banana\n", "sandía\n", "pera"]
with open("prueba3.bin", "wb") as archivo:
    for i in lista:
        archivo.write(i.encode("utf-8"))

with open("prueba3.bin", "rb") as archivo:
    contenido = archivo.read().decode("utf-8")
    print(contenido)

print("\n")

# 2. Lista de elementos a un archivo binario FORMA 2
lista = ["manzana", "banana", "sandía", "pera"]
with open("prueba3.bin", "wb") as archivo:
    for i in lista:
        if i != lista[-1]:
            i = i + "\n"
        archivo.write(i.encode("utf-8"))

with open("prueba3.bin", "rb") as archivo:
    contenido = archivo.read().decode("utf-8")
    print(contenido)