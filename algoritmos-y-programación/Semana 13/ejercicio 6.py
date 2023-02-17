# Ejercicio 6

cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# Crear listas:
miLista1 = []
miLista2 = []
miLista3 = []

# Llenar lista 1:
for i in range(cantidad_elementos):
    elemento = eval(input(f"Ingrese el elemento miLista1[{i}]: "))
    miLista1.append(elemento)

# Llenar lista 2:
for i in range(cantidad_elementos):
    elemento = eval(input(f"Ingrese el elemento miLista2[{i}]: "))
    miLista2.append(elemento)

x = len(miLista2)
for i in range(cantidad_elementos):
    suma_elementos = miLista1[i] + miLista2[(x - (i + 1))]
    miLista3.append(suma_elementos)

# Resultados:
print("- - RESULTADOS - -")
print("Lista 1: ", miLista1)
print("Lista 2: ", miLista2)
print("Lista 3: ", miLista3)