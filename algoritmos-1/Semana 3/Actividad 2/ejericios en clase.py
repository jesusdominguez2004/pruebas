# Semana 3 | Algoritmos 1 | Jesús Domínguez

# Instalar módulo numpy
"""
python3 -m pip install numpy

cmd: pip install numpy
"""
# Importar módulo numpy
import numpy as np

# Definir la cantidad de filas y columnas
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 3 x 3

# Imprimir toda la matriz
print("- - MATRIZ ESTÁTICA - -")
print(m1)

# Imprimir todas las filas
print("- - - -")
print(m1[0])
print(m1[1])
print(m1[2])

# Imprimir todas las columnas
print("- - - -")
print(m1[0][0])
print(m1[0][1])
print(m1[0][2])
print(m1[1][0])
print(m1[1][1])
print(m1[1][2])
print(m1[2][0])
print(m1[2][1])
print(m1[2][2])

# 1) Sumatoria de elementos columna 0
print("- - - -")
print(f"Mi m1[0][0]: {m1[0][0]}")
print(f"Mi m1[1][0]: {m1[1][0]}")
print(f"Mi m1[2][0]: {m1[2][0]}")
print(f"Sumatoria: {m1[0][0] + m1[1][0] + m1 [2][0]}")

# 2) Sumatoria elementos de la matriz
print("- - - -")
print(f"Filas: {len(m1)}")
print(f"Columnas: {len(m1[0])}")

# Definir acumulador
sumatoria = 0
# Recorrer filas
for i in range(len(m1)):
    # Recorrer columnas
    for j in range(len(m1[0])):
        # m1[fila][columna]
        sumatoria = sumatoria + m1[i][j]

# Imprimir resutado
print(f"Sumatoria elementos: {sumatoria}")

# 3) Elemento mayor y menor de la matriz
print("- - - -")
elemento_mayor = m1[0][0]
elemento_menor = m1[0][0]

# Recorrer filas
for i in range(len(m1)):
    # Recorrer columnas
    for i in range(len(m1[0])):
        # Mayor
        if m1[i][j] > elemento_mayor:
            elemento_mayor = m1[i][j]
        # Menor
        if m1[i][j] < elemento_menor:
            elemento_menor = m1[i][j]

print(f"Elemento mayor: {elemento_mayor}")
print(f"Elemento menor: {elemento_menor}")

# 4) Cantidad números positivos y negativos
print("- - - -")
cantidad_positivos = 0
cantidad_negativos = 0

# Recorrer filas
for i in range(len(m1)):
    # Recorrer columnas
    for j in range(len(m1[0])):
        # Positivos
        if m1[i][j] > 0:
            cantidad_positivos = cantidad_positivos + 1
        # Negativos
        if m1[i][j] < 0:
            cantidad_negativos = cantidad_negativos + 1

print(f"Cantidad positivos: {cantidad_positivos}")
print(f"Cantidad negativos: {cantidad_negativos}")

# 5) Promedio elementos
print("- - - -")
sumatoria_elementos = 0

# Recorrer filas
for i in range(len(m1)):
    # Recorrer columnas
    for j in range(len(m1[0])):
        sumatoria_elementos = sumatoria_elementos + m1[i][j]

# Evitar división por cero
if sumatoria_elementos == 0:
    print("Promedio de elementos: 0")
else:
    promedio_elementos = round(sumatoria_elementos / (len(m1) * len(m1[0])), 2)
    print(f"Promedio de elementos: {promedio_elementos}")

# 6) Sumatoria diagonal principal de la matriz
print("- - - -")

# SIN CONDICIONALES
sumatoria_diagonal = 0
# Recorrer filas
for i in range(len(m1)): 
    sumatoria_diagonal = sumatoria_diagonal + m1[i][i]
print(f"Sumatoria diagonal principal (SIN CONDICIONAL): {sumatoria_diagonal}")

# CON CONDICIONALES
sumatoria_diagonal = 0
# Recorrer filas
for i in range(len(m1)): 
    # Recorrer columnas
    for j in range(len(m1[0])): 
        # Comparar j con i
        if j == i:
            sumatoria_diagonal = sumatoria_diagonal + m1[i][j]
print(f"Sumatoria diagonal principal (CON CONDICIONAL): {sumatoria_diagonal}")


# 7) Cuál es mayor sumatoria diagonal principal o secundaria
print("- - - -")

sumatoria_diagonal_principal = 0

# Recorrer filas
for i in range(len(m1)): 
    # Recorrer columnas
    for j in range(len(m1[0])):
        # Comparar j con i
        if j == i:
            sumatoria_diagonal_principal = sumatoria_diagonal_principal + m1[i][j]

sumatoria_diagonal_secundaria = 0
j = 0
# Recorrer filas
for i in range(len(m1)): 
    sumatoria_diagonal_secundaria = sumatoria_diagonal_secundaria + m1[i][2-j]
    j = j + 1

print(f"Sumatoria diagonal principal: {sumatoria_diagonal_principal}")  
print(f"Sumatoria diagonal secundaria: {sumatoria_diagonal_secundaria}") 

if sumatoria_diagonal_principal > sumatoria_diagonal_secundaria:
    print("¡La sumatoria de la diagonal principal es mayor!")
elif sumatoria_diagonal_principal < sumatoria_diagonal_secundaria:
    print("¡La sumatoria de la diagonal secundaria es mayor!")
else:
    print("¡Ambas diagonales son iguales!")
    
# # # # # # # # # # # # # # # #

# Matriz dinámica normal
print("- - MATRIZ ESTÁTICA - -")

# Definir filas y columnas
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columna: "))

# Crear matriz
m2 = np.zeros([filas, columnas])

# Llenar matriz
for i in range(filas):
    for j in range(columnas):
        x = eval(input(f"Ingrese el elemento m2[{i}][{j}]: "))
        m2[i,j] = x

# Imprimir matriz
print("- - - -")
print(m2)

# 1) Promedio de elementos
print("- - - -")
sumatoria_elementos = 0

# Recorrer filas
for i in range(len(m2)):
    # Recorrer columnas
    for j in range(len(m2[0])):
        # Ir acumulando...
        sumatoria_elementos = sumatoria_elementos + m2[i][j]

# Procedimiento
promedio_elementos = round(sumatoria_elementos / (len(m2) * len(m2[0])), 2)

# Imprimir resultados
print(f"Promedio de elementos: {promedio_elementos}")

# 2) Sumatoria diagonal principal matriz
print("- - - -")
sumatoria_diagonal_principal = 0

# Recorrer filas
for i in range(len(m2)): 
    # Recorrer columnas
    for j in range(len(m2[0])): 
        # Comparar j con i
        if j == i:
            # Ir acumulando...
            sumatoria_diagonal_principal = sumatoria_diagonal_principal + m2[i][j]

# Imprimir resultados
print(f"Sumatoria diagonal principal: {sumatoria_diagonal_principal}")

# 3) Cuál es mayor sumatoria principal o secundaria de la matriz

# - - Calcular diagonal principal - -
print("- - - -")
sumatoria_diagonal_principal = 0

# Recorrer filas
for i in range(len(m2)): 
    # Recorrer columnas
    for j in range(len(m2[0])): 
        # Comparar j con i
        if j == i:
            # Ir acumulando...
            sumatoria_diagonal_principal = sumatoria_diagonal_principal + m2[i][j]

# - - Calcular diagonal secundaria - -
sumatoria_diagonal_secundaria = 0
j = 0
# Recorrer filas
for i in range(len(m2)): 
    sumatoria_diagonal_secundaria = sumatoria_diagonal_secundaria + m2[i][len(m2[0]) - 1 - j]
    j = j + 1


# Imprimir resultados
print(f"Sumatoria diagonal principal: {sumatoria_diagonal_principal}")
print(f"Sumatoria diagonal secundaria: {sumatoria_diagonal_secundaria}")

if sumatoria_diagonal_principal > sumatoria_diagonal_secundaria:
    print("¡La sumatoria de la diagonal principal es mayor!")
elif sumatoria_diagonal_principal < sumatoria_diagonal_secundaria:
    print("¡La sumatoria de la diagonal secundaria es mayor!")
else:
    print("¡Ambas diagonales son iguales!")