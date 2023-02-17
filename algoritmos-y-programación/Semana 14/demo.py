# Bucle While

# Definir variable de control:
i = 0
# Bucle condición:
while i <= 10:
    # Instrucción:
    print(i) 
    # Incrementar variable de valor manualmente:
    i = i + 1

# 1) Llenar una lista con While:
cantidad = eval(input("Ingrese la cantidad de elementos: "))

a = []
x = 0
while x < cantidad:
    elemento = eval(input(f"Ingrese el elemento a[{x}]: "))
    a.append(elemento)
    x = x + 1
print(a)

# 2) Cuántos números positivos y negativos en lista A:
i = 0
positivos = 0
negativos = 0
ceros = 0

while i < len(a):
    if a[i] > 0:
        positivos = positivos + 1
    elif a[i] < 0:
        negativos = negativos + 1
    else:
        ceros = ceros + 1
    i = i + 1

print("Números positivos:", positivos)
print("Números negativos:", negativos)
print("Ceros:", ceros)

# 3) Sumatoria de números positivos y números negativos:
i = 0
suma_positivos = 0
suma_negativos = 0

while i < len(a):
    if a[i] > 0:
        suma_positivos = suma_positivos + a[i]

    if a[i] < 0:
        suma_negativos = suma_negativos + a[i]
        
    i = i + 1

print("Sumatoria positivos:", suma_positivos)
print("Sumatoria negativos:", suma_negativos)