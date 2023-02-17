# Ejercicio 2 | Tipo A

n = int(input(">>> Ingrese tamaño vector: "))

vector = []
i = 0
while i < n:
    x = eval(input(f">>> Ingrese elemento vector[{i}]: "))
    vector.append(x)
    i = i + 1

pares_diez = 0
i = 0
while i < len(vector):
    if vector[i] % 2 == 0 and vector[i] > 10:
        pares_diez = pares_diez + 1
    i = i + 1

suma = 0
i = 0
while i < len(vector):
    suma = suma + vector[i]
    i = i + 1
promedio = suma / len(vector)
promedio = round(promedio, 2)

print(f"<<< Pares mayores que 10: {pares_diez}")
print(f"<<< Promedio elementos: {promedio}")
