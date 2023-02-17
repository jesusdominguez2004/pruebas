# Ejercicio 3

cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# Crear listas:
miLista1 = []
miLista2 = []

# Llenar lista 1:
for i in range(cantidad_elementos):
    elemento = eval(input(f"Ingrese el elemento miLista1[{i}]: "))
    miLista1.append(elemento)

# Llenar lista 2:
for i in range(cantidad_elementos):
    elemento = eval(input(f"Ingrese el elemento miLista2[{i}]: "))
    miLista2.append(elemento)

# Mayor elemento de lista 1:
mayor_lista1 = miLista1[0]
contador1 = 0
posicion_elemento1 = 0

for i in miLista1:
    contador1 = contador1 + 1
    if i > mayor_lista1:
        mayor_lista1 = i
        posicion_elemento1 = contador1 - 1

# Mayor elemento de lista 2:
mayor_lista2 = miLista2[0]
contador2 = 0
posicion_elemento2 = 0

for i in miLista2:
    contador2 = contador2 + 1
    if i > mayor_lista2:
        mayor_lista2 = i
        posicion_elemento2 = contador2 - 1

# Imprimir listas:
print("- - RESULTADOS - -")
print("Lista 1: ", miLista1)
print("Lista 2: ", miLista2)

# Imprimir elementos mayores:
print("Elemento mayor lista 1: ", mayor_lista1, "(miLista1[", posicion_elemento1, "])")
print("Elemento mayor lista 2: ", mayor_lista2, "(miLista2[", posicion_elemento2, "])")

# Comparar elementos mayores de ambas listas:
if mayor_lista1 > mayor_lista2:
    print("El elemento mayor de los dos está en lista 1...")
elif mayor_lista1 < mayor_lista2:
    print("El elemento mayor de los dos está en lista 2...")
else:
    print("Los elementos mayores son iguales en ambas listas...")