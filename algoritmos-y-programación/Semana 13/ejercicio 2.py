# Ejercicio 2

cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# Crear lista:
miLista = []

# Llenar lista:
for i in range(cantidad_elementos):
    elemento = eval(input(f"Ingrese el elemento miLista[{i}]: "))
    miLista.append(elemento)

# Mayor y menor inicial:
mayor = miLista[0]
menor = miLista[0]

for i in miLista:
    
    if i > mayor:
        mayor = i
    if i < menor:
        menor = i

print("Elemento mayor: ", mayor)
print("Elemento menor: ", menor)