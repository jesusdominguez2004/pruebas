# Ejercicio 1 | Matrices

# Definir la matriz
ventas = [] # [[Código, usuario, producto, total], [Código, usuario, producto, total], ... ]

# Cantidad de ventas
cantidad_ventas = input("Ingrese la cantidad de ventas: ")

# Validar
while not cantidad_ventas.isnumeric():
    print("Datos no válidos...")
    cantidad_ventas = input("Ingrese la cantidad de ventas nuevamente: ")

# Recorrer registros (filas)
i = 0
while i < int(cantidad_ventas):

    # Agregar fila vacia
    ventas.append([])

    # Recorrer datos (columnas)
    j = 0
    while j < 5:
        nombre_usuario = input(f"Ingrese nombre del usuario {i + 1}: ")
        # Cambiar datos (columna)
        j = j + 1

    # Agregar
    ventas[i].append("1")
    ventas[i].append("2")
    ventas[i].append("3")
    ventas[i].append("4")

    # Cambiar registro (fila)    
    i = i + 1

# Imprimir ventas
print(ventas)