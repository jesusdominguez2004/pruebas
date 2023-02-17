# Usando with

# 1. Crear un archivo binario
with open("prueba2.bin", "wb") as archivo:
    archivo.write(b"Hola mundo\n")
    archivo.write(b"Esto es un archivo binario\n")
    archivo.write(b"Python 3.11")

# 2. Leer información con read()
with open("prueba2.bin", "rb") as archivo:
    contenido = archivo.read().decode("utf-8")
    print(contenido)

# 3. Leer información con un ciclo for
print("\n")
with open("prueba2.bin", "rb") as archivo:
    for linea in archivo:
        print(linea.decode("utf-8"), end="")

# 4. Obtener una lista de las lineas y usar for
print("\n")
with open("prueba2.bin", "rb") as archivo:
    lienas = archivo.readlines()
    print(lienas)
    for linea in lienas:
        print(linea.decode("utf-8"), end="")

# 5. Obtener una lista de las lineas y usar while
print("\n")
with open("prueba2.bin", "rb") as archivo:
    lienas = archivo.readlines()
    print(lienas)
    i = 0
    while i < len(lienas):
        print(lienas[i].decode("utf-8"), end="")
        i = i + 1