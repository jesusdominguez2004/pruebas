# Tarea Luis González

from random import randint

numeros = []

for i in range(100):
    x = randint(1, 100)
    numeros.append(x)

    if x % 2 == 0:
        try:
            archivo_pares = open("pares.txt", "a")
            archivo_pares.write(f"{x} ")
        except:
            print("pares.txt no existe, archivo creado...")

    if x % 2 != 0:
        try:
            archivo_impares = open("impares.txt", "a")
            archivo_impares.write(f"{x} ")
        except:
            print("impares.txt no existe, archivo creado...")

try:
    archivo_pares = open("pares.txt", "r")
    archivo_impares = open("impares.txt", "r")

    contenido_pares = archivo_pares.read()
    contenido_impares = archivo_impares.read()

    pares = contenido_pares.split(" ")
    impares = contenido_impares.split(" ")

    pares.pop()
    impares.pop()

    suma_pares = 0
    for i in range(len(pares)):
        suma_pares = suma_pares + int(pares[i])
    print(f"\033[0;32mSuma pares: \033[1;32m{suma_pares}")

    suma_impares = 0
    for i in range(len(impares)):
        suma_impares = suma_impares + int(impares[i])
    print(f"\033[0;36mSuma impares: \033[1;36m{suma_impares}")

    archivo_pares.close()
    archivo_impares.close()

    # print(pares)
    # print(impares)
    # print(type(contenido_pares), contenido_pares)
    # print(type(contenido_impares), contenido_impares)
except:
    print("Archivo(s) no encontrado, creando archivo(s)...")