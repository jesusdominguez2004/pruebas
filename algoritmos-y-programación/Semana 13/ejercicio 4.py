# Ejercicio 4 | Invertir elementos de una lista

cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# Crear listas:
miLista = []
miListaInvertida = []

# Llenar lista:
for i in range(cantidad_elementos):
    elemento = eval(input(f"Ingrese el elemento miLista[{i}]: "))
    miLista.append(elemento)

# Invertir elementos:
miLista.reverse()
miListaInvertida = miLista

# Resultados:
print(miListaInvertida)