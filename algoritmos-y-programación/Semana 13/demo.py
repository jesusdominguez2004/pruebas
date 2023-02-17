# Capturar de la cantidad de elementos:
cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# Llenado de vector o lista:
a = []
for i in range(cantidad_elementos):
    valor = eval(input("Ingrese un elemento: "))
    a.append(valor)

# Mostrar la lista:
print(a)

# 1) Contar elementos + y - de la lista:
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0

for i in a:
    if i > 0:
        contador_positivos = contador_positivos + 1
    elif i == 0:
        contador_ceros = contador_ceros + 1
    else:
        contador_negativos = contador_negativos + 1

print("La cantidad de números positivos es: ", contador_positivos)
print("La cantidad de números negativos es: ", contador_negativos)
print("La cantidad de números ceros es: ", contador_ceros)

# 2) Promedio de elementos de la lista:
acumulador = 0

for i in a:
    acumulador = acumulador + i

promedio = acumulador / len(a)

print("La sumatorio de los elementos de la lista es: ", acumulador)
print("La cantidad de elementos de la lista es: ", len(a))
print("El promedio de los elementos de la lista es: ", promedio)