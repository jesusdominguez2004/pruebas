# Ejercicio 1 | Práctica

# 1) Dado un vector...
print("- - PUNTO 1 - - ")
mi_vector = []

# Preguntar número de elementos
cantidad_elementos = input("Ingrese la cantidad de elementos para mi_vector[]: ") # str

# Validar
while not cantidad_elementos.isnumeric() or cantidad_elementos == "0":
    print("Datos no validos...")
    cantidad_elementos = input("Ingrese la cantidad de elementos para mi_vector[]: ") # str

# Llenar vector
i = 0
while i < int(cantidad_elementos):
    # Preguntar elemento
    x = eval(input(f"Ingrese el elemento mi_vector[{i}]: "))
    # Añadir elemento
    mi_vector.append(x)
    # Modificar variable de control
    i = i + 1

# Elemento mayor y elemento menor
elemento_mayor = mi_vector[0]
elemento_menor = mi_vector[0]

i = 0
while i < int(cantidad_elementos):
    # Mayor
    if mi_vector[i] > elemento_mayor:
        elemento_mayor = mi_vector[i]
    # Menor
    if mi_vector[i] < elemento_menor:
        elemento_menor = mi_vector[i]
    # Modificar variable de control
    i = i + 1

# Resultados
print(f"Mi vector: {mi_vector}")
print(f"Elemento mayor: {elemento_mayor}")
print(f"Elemento menor: {elemento_menor}")

# 2) Realice un algoritmo...
print("- - PUNTO 2 - - ")
mi_vector = []

# Preguntar número de elementos
cantidad_elementos = input("Ingrese la cantidad de elementos para mi_vector[]: ") # str

# Validar
while not cantidad_elementos.isnumeric() or cantidad_elementos == "0":
    print("Datos no validos...")
    cantidad_elementos = input("Ingrese la cantidad de elementos para mi_vector[]: ") # str

# Llenar vector
i = 0
while i < int(cantidad_elementos):
    # Preguntar elemento
    x = eval(input(f"Ingrese el elemento mi_vector[{i}]: "))
    # Añadir elemento
    mi_vector.append(x)
    # Modificar variable de control
    i = i + 1

# Elementos pares mayores que diez
contador = 0
a = []
i = 0
while i < int(cantidad_elementos):
    # Par and mayor que 10
    if abs(mi_vector[i]) % 2 == 0 and mi_vector[i] > 10:
        contador = contador + 1
        a.append(mi_vector[i])
    i = i + 1

# Promedio
sumatoria_elementos = 0
i = 0
while i < int(cantidad_elementos):
    # Ir sumando los elementos
    sumatoria_elementos = sumatoria_elementos + mi_vector[i]
    i = i + 1
# Calcular
promedio_elementos = round(sumatoria_elementos / int(cantidad_elementos), 2)

# Resultados
print(f"Mi vector: {mi_vector}")
if len(a) == 0:
    print(f"Elementos pares mayores que diez: {contador}")
else:
    print(f"Elementos pares mayores que diez: {contador}", end=" (")
    i = 0
    while i < len(a):
        # Sino es el último
        if not i == len(a) - 1:
            print(a[i], end=", ")
        # Si es el último
        else:
            print(str(a[i]) + ")")
        # Modificar variable de control
        i = i + 1
print(f"Promedio de elementos: {promedio_elementos}") 