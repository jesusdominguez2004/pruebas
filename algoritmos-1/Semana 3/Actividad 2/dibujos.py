# Dibujar letras | Semana 3 | Jesús Domínguez

# PASO 1 - Importar módulo numpy

# PASO 2 - Crear matricez 5x5
matriz_u = [["*", " ", " ", " ", "*"], ["*", " ", " ", " ", "*"], ["*", " ", " ", " ", "*"], ["*", " ", " ", " ", "*"], ["*", "*", "*", "*", "*"]]
matriz_o = [["*", "*", "*", "*", "*"], ["*", " ", " ", " ", "*"], ["*", " ", " ", " ", "*"], ["*", " ", " ", " ", "*"], ["*", "*", "*", "*", "*"]]
matriz_l = [["*", " ", " ", " ", " "], ["*", " ", " ", " ", " "], ["*", " ", " ", " ", " "], ["*", " ", " ", " ", " "], ["*", "*", "*", "*", "*"]]
matriz_n = [["*", " ", " ", " ", "*"], ["*", "*", " ", " ", "*"], ["*", " ", "*", " ", "*"], ["*", " ", " ", "*", "*"], ["*", " ", " ", " ", "*"]]
matriz_c = [["*", "*", "*", "*", "*"], ["*", " ", " ", " ", " "], ["*", " ", " ", " ", " "], ["*", " ", " ", " ", " "], ["*", "*", "*", "*", "*"]]
matriz_x = [["*", " ", " ", " ", "*"], [" ", "*", " ", "*", " "], [" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", " ", " ", " ", "*"]]
matriz_z = [["*", "*", "*", "*", "*"], [" ", " ", " ", "*", " "], [" ", " ", "*", " ", " "], [" ", "*", " ", " ", " "], ["*", "*", "*", "*", "*"]]

# PASO 3 - Dibujar

# Recorrer filas
for i in range(len(matriz_u)):
    # Recorrer columnas
    for j in range(len(matriz_u)):
        # Ir imprimiendo columnas
        print(matriz_u[i][j], end=" ")
    # Cambiar fila
    print("")
# Separador
print("- - - - -")

# Recorrer filas
for i in range(len(matriz_o)):
    # Recorrer columnas
    for j in range(len(matriz_o)):
        # Ir imprimiendo columnas
        print(matriz_o[i][j], end=" ")
    # Cambiar fila
    print("")
# Separador
print("- - - - -")

# Recorrer filas
for i in range(len(matriz_l)):
    # Recorrer columnas
    for j in range(len(matriz_l)):
        # Ir imprimiendo columnas
        print(matriz_l[i][j], end=" ")
    # Cambiar fila
    print("")
# Separador
print("- - - - -")

# Recorrer filas
for i in range(len(matriz_n)):
    # Recorrer columnas
    for j in range(len(matriz_n)):
        # Ir imprimiendo columnas
        print(matriz_n[i][j], end=" ")
    # Cambiar fila
    print("")
# Separador
print("- - - - -")

# Recorrer filas
for i in range(len(matriz_c)):
    # Recorrer columnas
    for j in range(len(matriz_c)):
        # Ir imprimiendo columnas
        print(matriz_c[i][j], end=" ")
    # Cambiar fila
    print("")
# Separador
print("- - - - -")

# Recorrer filas
for i in range(len(matriz_x)):
    # Recorrer columnas
    for j in range(len(matriz_x)):
        # Ir imprimiendo columnas
        print(matriz_x[i][j], end=" ")
    # Cambiar fila
    print("")
# Separador
print("- - - - -")

# Recorrer filas
for i in range(len(matriz_z)):
    # Recorrer columnas
    for j in range(len(matriz_z)):
        # Ir imprimiendo columnas
        print(matriz_z[i][j], end=" ")
    # Cambiar fila
    print("")