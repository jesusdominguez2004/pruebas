# Semana 2 | Algoritmos I

# 1) Crear un vecector estático
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Vector a:", a)

# 2) Crear un vector y llenarlo de forma manual
b = []
b.append(10)
b.append(20)
b.append(30)
b.append(40)
b.append(50)
b.append(60)
b.append(70)
b.append(80)
b.append(90)
b.append(100)
print("Vector b:", b)

# 3) Crear un vector dinámico y el usuario ingresa los valores
n = eval(input("Ingrese la cantidad de elementos: "))
c = []

for i in range(n):
    valor = eval(input(f"Ingrese un elemento en la posición c[{i}]: "))
    c.append(valor)

print("Vector c:", c)

# 4) Primer y último elemento
print(f"Primer elemento c: {c[0]}")
print(f"Último elemento c: {c[len(c) - 1]}")

# 5) Promedio
sumatoria_elementos = 0
i = 0
while i < n:
    sumatoria_elementos = sumatoria_elementos + c[i]
    i = i + 1

promedio = sumatoria_elementos / n
print(f"Promedio elementos: {promedio}")

# 6) Promedio positivos y negativos
sumatoria_positivos = 0 # Acumulador
sumatoria_negativos = 0 # Acumulador
cantidad_positivos = 0 # Contador
cantidad_negativos = 0 # Contador

i = 0
while i < n:
    # Positivos
    if c[i] > 0:
        sumatoria_positivos = sumatoria_positivos + c[i]
        cantidad_positivos = cantidad_positivos + 1
    # Negativos
    else:
        sumatoria_negativos = sumatoria_negativos + c[i]
        cantidad_negativos = cantidad_negativos + 1
    i = i + 1

# Evitar divisón por cero
if cantidad_positivos != 0:
    promedio_positivos = sumatoria_positivos / cantidad_positivos
    print(f"Promedio positivos: {promedio_positivos}")
else:
    print("Promedio positivos: 0")

# Evitar divisón por cero
if cantidad_negativos != 0:
    promedio_negativos = sumatoria_negativos / cantidad_negativos
    print(f"Promedio negativos: {promedio_negativos}")
else:
    print("Promedio negativos: 0")

# 7) Máximo y mínimo
maximo = c[0]
minimo = c[0]

i = 0
while i < n:
    if c[i] > maximo:
        maximo = c[i]
    
    if c[i] < minimo:
        minimo = c[i]
    i = i + 1

print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")

# 8) Mostrar el vector de derecha a izquierda
print("Elementos de derecha a izquierda con while")
i = 0
while i < n:
    print(f"{c[n - 1 - i]}")
    i = i + 1
print("Elementos de derecha a izquierda con for")
for i in range(n - 1, -1, -1):
    print(f"{c[i]}")

# 9) Dado un valor decir si está o no dentro del vector y cuántas veces está
valor_buscar = eval(input("Ingrese un valor a buscar en c[]: "))
veces_encontrado = 0

i = 0
while i < n:
    # Buscar
    if valor_buscar == c[i]:
        # Contar
        veces_encontrado = veces_encontrado + 1
    i = i + 1

if veces_encontrado != 0:
    print(f"¡Sí se encontró el valor {valor_buscar}!")
    print(f"Veces encontrado: {veces_encontrado}")
else:
    print(f"No se encontró el valor {valor_buscar}...")
    print(f"Veces encontrado: {veces_encontrado}")

# 10) Dado un vector de números mostrar la tabla de multiplcar de dichos elementos
i = 0
while i < n: # Ciclo número
    print(f"- - Tabla del {c[i]} - -")
    x = 1
    while x <= 10: # Ciclo tabla
        print(f"{c[i]} x {x} = {c[i] * x}")
        x = x + 1
    i = i + 1