# Ejercicio 1 | Tipo A

n = int(input(">>> Ingrese tamaño vector: "))

vector = []
i = 0
while i < n:
    x = eval(input(f">>> Ingrese elemento vector[{i}]: "))
    vector.append(x)
    i = i + 1

mayor = vector[0]
menor = vector[0]
i = 0
while i < n:
    if vector[i] > mayor:
        mayor = vector[i]

    if vector[i] < menor:
        menor = vector[i]

    i = i + 1

print(f"<<< Número mayor: {mayor}")
print(f"<<< Número menor: {menor}")
