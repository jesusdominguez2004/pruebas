# Ejercicio 5

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

# Invertir miLista2:
miLista2.reverse()

# Llenar miLista3:
miLista3 = []
for i in range(cantidad_elementos):
    suma_elementos = miLista1[i] + miLista2[i]
    miLista3.append(suma_elementos)

# Restablecer orden miLista2:
miLista2.reverse()

# Resultados:
print("- - RESULTADOS - -")
print("Lista 1: ", miLista1)
print("Lista 2: ", miLista2)
print("Lista 3: ", miLista3)