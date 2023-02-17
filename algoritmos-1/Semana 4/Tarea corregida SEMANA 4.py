# Ejercicio 1 | Semana 4 | Jesús Domínguez

# Crear matriz
matrix = []

# Crear lista de productos
mis_productos = ["Arroz", "Pastas", "Manzana", "Lentejas", "Uvas"]
lista_precios = [2500, 1600, 3000, 2300, 4000]
lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
listas_cc = []

# Cantidad de registros
print("- - SISTEMA DE matrix - -")
cantidad_registros = eval(input("Ingrese la cantidad de registros: "))

# Llenar matriz
i = 0
while i < cantidad_registros:
    # Agregar fila en blanco
    matrix.append([])

    # Ingresar datos
    dia = int(input(f"Ingrese el día (cliente {i+1}): "))
    mes = int(input(f"Ingrese el mes (cliente {i+1}): "))

    # Validar que mes exista
    while mes > len(lista_meses) or mes < 1:
        print("Datos no validos...")
        mes = int(input(f"Ingrese el mes (cliente {i+1}): "))

    mes = lista_meses[mes - 1]
    año = int(input(f"Ingrese el año (cliente {i+1}): "))

    # Validar CC
    cc = int(input(f"Ingrese la CC (cliente {i+1}): "))
    while cc in listas_cc:
        print("CC Repetida...")
        cc = int(input(f"Ingrese la CC (cliente {i+1}): "))
    listas_cc.append(cc)

    nombre_cliente = input(f"Ingrese el nombre cliente (cliente {i+1}): ")

    # Imprimir lista de productos
    x = 0
    while x < len(mis_productos):
        print(f"{x + 1} = {mis_productos[x]}")
        x = x + 1
    producto = int(input(f"Ingrese el producto (cliente {i+1}): "))

    # Validar que producto escogido exista
    while producto > len(mis_productos) or producto < 1:
        print("Datos no validos...")
        producto = int(input(f"Ingrese el producto (cliente {i+1}): "))    

    cantidad = int(input(f"Ingrese la cantidad (cliente {i+1}): "))

    # Validar que cantidad sea mayor que 0
    while cantidad < 1:
        print("Datos no validos...")
        cantidad = int(input(f"Ingrese la cantidad (cliente {i+1}): "))
  
    valor_unitario = lista_precios[producto - 1]
    producto = mis_productos[producto - 1]
    total = cantidad * valor_unitario
    print("- - - -")

    # Almacenar datos
    matrix[i].append(i + 1)
    matrix[i].append(dia)
    matrix[i].append(mes)
    matrix[i].append(año)
    matrix[i].append(cc)
    matrix[i].append(nombre_cliente)
    matrix[i].append(producto)
    matrix[i].append(cantidad)
    matrix[i].append(valor_unitario)
    matrix[i].append(total)

    # Cambiar de fila
    i = i + 1

# Imprimir matriz
print(matrix)

# 1) Calcule el total de matrix
print("- - - -")
total_matrix = 0

# Recorrer registros
i = 0
while i < cantidad_registros:
    # Ir acumulando
    total_matrix = total_matrix + matrix[i][9]
    # Cambiar registros
    i = i + 1

# Imprimir resultado
print(f"Total de matrix: ${total_matrix}")

# 2) Calcule el producto más vendido
print("- - - -")
print("Productos vendidos:")

# Contar cada tipo producto vendido
conteo_productos = []
contador = 0
i = 0
while i < len(mis_productos):

    # Recorrer registros
    j = 0
    while j < cantidad_registros:
        # Si encontró i producto
        if mis_productos[i] == matrix[j][6]:
            contador = contador + matrix[j][7]
        # Cambiar registro
        j = j + 1

    # Agregar valor contador en una lista
    conteo_productos.append(contador)
    # Restablecer contador
    contador = 0
    # Cambiar producto a buscar
    i = i + 1

# Imprimir productos y sus cantidades
i = 0
while i < len(mis_productos):
    print(f"{i + 1}. {mis_productos[i]} (cantidad {conteo_productos[i]})")
    i = i + 1

# Identificar el mayor
mas_vendido = conteo_productos[0]
nombre_producto = mis_productos[0]

i = 0
while i < len(conteo_productos):
    if conteo_productos[i] > mas_vendido:
        mas_vendido = conteo_productos[i]
        nombre_producto = mis_productos[i]
    i = i + 1

# Validar que no hallan máximos iguales
contador = 0
i = 0 
while i < len(conteo_productos):
    if conteo_productos[i] == mas_vendido:
        contador = contador + 1
    i = i + 1
print("")

# Si solo hay un máximo
if contador == 1:
    print("Producto más vendido:")
    print(f"{nombre_producto} (cantidad {mas_vendido})")
# Si hay varios máximos:
else:
    print("¡Hay máximos iguales!")
    print("Los más vendidos fueron: ")
    i = 0
    while i < len(conteo_productos):
        if conteo_productos[i] == mas_vendido:
            print(f"{mis_productos[i]} (cantidad {mas_vendido})")
        i = i + 1

# 3) Calcule el promedio de matrix en un mes y año especificado
print("- - - -")
año_buscar = int(input("Ingrese año a buscar: "))
mes_buscar = int(input("Ingrese mes a buscar: "))

acumulador = 0
contador = 0

# Recorrer registros
i = 0
while i < cantidad_registros:

    # Si año_buscar == año_registrado... and Si mes_buscar == mes_registrado...
    if año_buscar == matrix[i][3] and mes_buscar == matrix[i][2]:
        # Ir acumulando
        acumulador = acumulador + matrix[i][9]
        contador = contador + 1
    # Cambiar registro
    i = i + 1
print("")

# Dividir
if contador != 0:
    promedio = round(acumulador / contador, 2)
    print(f"Promedio matrix de año {año_buscar} mes {mes_buscar}: ${promedio}")
else:
    print("No hubo matrix en esa fecha...")
    print(f"Promedio matrix de año {año_buscar} mes {mes_buscar}: $0")

# 4) Año con mayor matrix
print("- - - -")
print("Años registrados:")

# Crear una lista de años
lista_años = []

# Recorrer registros
i = 0
while i < cantidad_registros:
    # Validar
    if matrix[i][3] not in lista_años:
        lista_años.append(matrix[i][3])
    # Cambiar registro
    i = i + 1 

# Contar cada año registrado
matrix_años = []
acumulador = 0
i = 0
while i < len(lista_años):

    # Recorrer registros
    j = 0
    while j < cantidad_registros:
        # Si encontró i año
        if lista_años[i] == matrix[j][3]:
            # Ir acumulando matrix
            acumulador = acumulador + matrix[j][9]
        # Cambiar registro
        j = j + 1

    # Agregar valor acumulador en una lista
    matrix_años.append(acumulador)
    # Restablecer acumulador
    acumulador = 0
    # Cambiar año a buscar
    i = i + 1

# Imprimir años y sus matrix
i = 0
while i < len(lista_años):
    print(f"{i + 1}. {lista_años[i]} (matrix ${matrix_años[i]})")
    i = i + 1

# Identificar el mayor
mayor_venta = matrix_años[0]
nombre_año = lista_años[0]

i = 0
while i < len(matrix_años):
    if matrix_años[i] > mayor_venta:
        mayor_venta = matrix_años[i]
        nombre_año = lista_años[i]
    i = i + 1

# Validar que no hallan máximos iguales
contador = 0
i = 0 
while i < len(matrix_años):
    if matrix_años[i] == mayor_venta:
        contador = contador + 1
    i = i + 1
print("")

# Si solo hay un máximo
if contador == 1:
    print("Año con más matrix:")
    print(f"{nombre_año} (matrix ${mayor_venta})")
# Si hay varios máximos:
else:
    print("¡Hay máximos iguales!")
    print("Años con mayor matrix: ")
    i = 0
    while i < len(matrix_años):
        if matrix_años[i] == mayor_venta:
            print(f"{lista_años[i]} (matrix ${mayor_venta})")
        i = i + 1

# 5) Mes con mayor matrix
print("- - - -")
print("Meses registrados:")

# Crear una lista de meses
lista_meses = []

# Recorrer registros
i = 0
while i < cantidad_registros:
    # Validar
    if matrix[i][2] not in lista_meses:
        lista_meses.append(matrix[i][2])
    # Cambiar registro
    i = i + 1 

# Contar cada mes registrado
matrix_meses = []
acumulador = 0
i = 0
while i < len(lista_meses):

    # Recorrer registros
    j = 0
    while j < cantidad_registros:
        # Si encontró i mes
        if lista_meses[i] == matrix[j][2]:
            # Ir acumulando matrix
            acumulador = acumulador + matrix[j][9]
        # Cambiar registro
        j = j + 1

    # Agregar valor acumulador en una lista
    matrix_meses.append(acumulador)
    # Restablecer acumulador
    acumulador = 0
    # Cambiar mes a buscar
    i = i + 1

# Imprimir meses y sus matrix
i = 0
while i < len(lista_meses):
    print(f"{i + 1}. {lista_meses[i]} (matrix ${matrix_meses[i]})")
    i = i + 1

# Identificar el mayor
mayor_venta = matrix_meses[0]
nombre_mes = lista_meses[0]

i = 0
while i < len(matrix_meses):
    if matrix_meses[i] > mayor_venta:
        mayor_venta = matrix_meses[i]
        nombre_mes = lista_meses[i]
    i = i + 1

# Validar que no hallan máximos iguales
contador = 0
i = 0 
while i < len(matrix_meses):
    if matrix_meses[i] == mayor_venta:
        contador = contador + 1
    i = i + 1
print("")

# Si solo hay un máximo
if contador == 1:
    print("Mes con más matrix:")
    print(f"{nombre_mes} (matrix ${mayor_venta})")
# Si hay varios máximos:
else:
    print("¡Hay máximos iguales!")
    print("Meses con mayor matrix: ")
    i = 0
    while i < len(matrix_meses):
        if matrix_meses[i] == mayor_venta:
            print(f"{lista_años[i]} (matrix ${mayor_venta})")
        i = i + 1

# 6) Buscar un cliente por cédula
print("- - - -")
cc_buscar = int(input("Ingrese CC a buscar: "))

# Recorrer registros
encontrado = False
i = 0
while i < cantidad_registros:
    # Ir buscando
    if cc_buscar == matrix[i][4]:
        encontrado = True
    
    # Cambiar registro
    i = i + 1

# Validar
if encontrado == False:
    print("Cliente no encontrado...")
else:
    print("¡Cliente encontrado!")
    i = 0
    while i < cantidad_registros:
        # Ir buscando
        if cc_buscar == matrix[i][4]:
            print(f"Nombre: {matrix[i][5]}")
        # Cambiar registro
        i = i + 1