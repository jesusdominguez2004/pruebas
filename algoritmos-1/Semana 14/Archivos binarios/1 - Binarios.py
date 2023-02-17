# Sin usar with

# 1. Crear un archivo binario
archivo = open("prueba1.bin", "wb")
archivo.write(b"Hola mundo\n")
archivo.write(b"Esto es un archivo binario\n")
archivo.write(b"Python 3.11")
archivo.close()

# 2. Leer información con read()
archivo = open("prueba1.bin", "rb")
contenido = archivo.read()
print(contenido.decode("utf-8"))
archivo.close()

# 3. Leer información con un ciclo for
print("\n")
archivo = open("prueba1.bin", "rb")
for linea in archivo:
    print(linea.decode("utf-8"), end="")
archivo.close()

# 4. Obtener una lista de las lineas y usar for
print("\n")
archivo = open("prueba1.bin", "rb")
lienas = archivo.readlines()
print(lienas)
for linea in lienas:
    print(linea.decode("utf-8"), end="")
archivo.close()

# 5. Obtener una lista de las lineas y usar while
print("\n")
archivo = open("prueba1.bin", "rb")
lienas = archivo.readlines()
print(lienas)
i = 0
while i < len(lienas):
    print(lienas[i].decode("utf-8"), end="")
    i = i + 1
archivo.close()