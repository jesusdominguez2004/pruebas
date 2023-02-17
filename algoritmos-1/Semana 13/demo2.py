"""try:
    informacion = open("ventas_enero.txt", "r+")
except:
    print("No existe el archivo")"""

# ARCHIVOS DE FORMA DINÁMICA

# 1. Nombres de los archivos
datos = ["ventas_enero.txt", "ventas_febrero.txt"]

# 2. Directorio
path = "Archivos/"

# 3. Generar rutas de cada archivo
for i in datos:
    archivo = path + i
    print(archivo)
    informacion = open(archivo, "r+")

    # 4. Promedio, mayor y menor de todos los archivos
    contador = 0
    acumulador = 0
    linea_0 = informacion.readline()
    mayor = int(linea_0)
    menor = int(linea_0)
    informacion = open(archivo, "r+")
    for j in informacion:
        acumulador = acumulador + int(j)
        contador = contador + 1

        if int(j) > mayor:
            mayor = int(j)

        if int(j) < menor:
            menor = int(j)
    
    promedio = acumulador / contador
    print(f"Cantidad elementos {i}: {contador}")
    print(f"Promedio {i}: {promedio}")
    print(f"Mayor {i}: {mayor}")
    print(f"Menor {i}: {menor}\n")

    # 5. Valores mayores y menores que x
    informacion = open(archivo, "r+")
    x = int(input("Ingrese un número: "))
    for i in informacion:
        if x > int(i):
            print(f"${i} es menor que ${x}")
        if x < int(i):
            print(f"${i} es mayor que ${x}")
    print("\n")

"""linea_1 = int(informacion.readline())
mayor = linea_1
menor = linea_1
informacion = open(path+datos[0], "r+")""" 