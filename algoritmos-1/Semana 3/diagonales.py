# Diagonales de una matriz n x n | Semana 3

# Crear matriz estática
matriz = [[8, 1, 32], [9, 2, 4], [5, 6, 0]]

# Diagonal principal
sumatoria = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if j == i:
            sumatoria = sumatoria + matriz[i][j]

print(f"Diagonal principal: {sumatoria}")

# Diagonal secundaria
sumatoria = 0
j = 0
for i in range(len(matriz)):
    sumatoria = sumatoria + matriz[i][len(matriz[0])- 1 - j]
    j = j + 1

print(f"Diagonal secundaria: {sumatoria}")