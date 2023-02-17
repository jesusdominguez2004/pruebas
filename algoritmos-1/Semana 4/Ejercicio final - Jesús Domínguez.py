# Ejercicio 1 | Semana 4 | Jesús Domínguez

# Crear matriz
ventas = []

# Crear lista de productos
lista_productos = ["Arroz", "Pastas", "Manzana", "Lentejas", "Uvas"]
lista_precios = [2500, 1600, 3000, 2300, 4000]
lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
listas_cc = []

# Cantidad de registros
print("- - SISTEMA DE VENTAS - -")
cantidad_registros = eval(input("Ingrese la cantidad de registros: "))

# Llenar matriz
i = 0
while i < cantidad_registros:
    # Agregar fila en blanco
    ventas.append([])

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
    while x < len(lista_productos):
        print(f"{x + 1} = {lista_productos[x]}")
        x = x + 1
    producto = int(input(f"Ingrese el producto (cliente {i+1}): "))

    # Validar que producto escogido exista
    while producto > len(lista_productos) or producto < 1:
        print("Datos no validos...")
        producto = int(input(f"Ingrese el producto (cliente {i+1}): "))    

    cantidad = int(input(f"Ingrese la cantidad (cliente {i+1}): "))

    # Validar que cantidad sea mayor que 0
    while cantidad < 1:
        print("Datos no validos...")
        cantidad = int(input(f"Ingrese la cantidad (cliente {i+1}): "))
  
    valor_unitario = lista_precios[producto - 1]
    producto = lista_productos[producto - 1]
    total = cantidad * valor_unitario
    print("- - - -")

    # Almacenar datos
    ventas[i].append(i + 1)
    ventas[i].append(dia)
    ventas[i].append(mes)
    ventas[i].append(año)
    ventas[i].append(cc)
    ventas[i].append(nombre_cliente)
    ventas[i].append(producto)
    ventas[i].append(cantidad)
    ventas[i].append(valor_unitario)
    ventas[i].append(total)

    # Cambiar de fila
    i = i + 1

# Imprimir matriz
print(ventas)

# 1) Calcule el total de ventas
print("- - - -")
total_ventas = 0

# Recorrer registros
i = 0
while i < cantidad_registros:
    # Ir acumulando
    total_ventas = total_ventas + ventas[i][9]
    # Cambiar registros
    i = i + 1

# Imprimir resultado
print(f"Total de ventas: ${total_ventas}")

# 2) Calcule el producto más vendido
print("- - - -")
print("Productos vendidos:")

# Contar cada tipo producto vendido
conteo_productos = []
contador = 0
i = 0
while i < len(lista_productos):

    # Recorrer registros
    j = 0
    while j < cantidad_registros:
        # Si encontró i producto
        if lista_productos[i] == ventas[j][6]: # NOMBRE PRODUCTO
            contador = contador + ventas[j][7] # CANTIDAD
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
while i < len(lista_productos):
    print(f"{i + 1}. {lista_productos[i]} (cantidad {conteo_productos[i]})")
    i = i + 1

# Identificar el mayor
mas_vendido = conteo_productos[0]
nombre_producto = lista_productos[0]

i = 0
while i < len(conteo_productos):
    if conteo_productos[i] > mas_vendido:
        mas_vendido = conteo_productos[i]
        nombre_producto = lista_productos[i]
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
            print(f"{lista_productos[i]} (cantidad {mas_vendido})")
        i = i + 1

# 3) Calcule el promedio de ventas en un mes y año especificado
print("- - - -")
año_buscar = int(input("Ingrese año a buscar: "))
mes_buscar = int(input("Ingrese mes a buscar: "))

acumulador = 0
contador = 0

# Recorrer registros
i = 0
while i < cantidad_registros:

    # Si año_buscar == año_registrado... and Si mes_buscar == mes_registrado...
    if año_buscar == ventas[i][3] and mes_buscar == ventas[i][2]:
        # Ir acumulando
        acumulador = acumulador + ventas[i][9]
        contador = contador + 1
    # Cambiar registro
    i = i + 1
print("")

# Dividir
if contador != 0:
    promedio = round(acumulador / contador, 2)
    print(f"Promedio ventas de año {año_buscar} mes {mes_buscar}: ${promedio}")
else:
    print("No hubo ventas en esa fecha...")
    print(f"Promedio ventas de año {año_buscar} mes {mes_buscar}: $0")

# 4) Año con mayor ventas
print("- - - -")
print("Años registrados:")

# Crear una lista de años
lista_años = []

# Recorrer registros
i = 0
while i < cantidad_registros:
    # Validar
    if ventas[i][3] not in lista_años:
        lista_años.append(ventas[i][3])
    # Cambiar registro
    i = i + 1 

# Contar cada año registrado
ventas_años = []
acumulador = 0
i = 0
while i < len(lista_años):

    # Recorrer registros
    j = 0
    while j < cantidad_registros:
        # Si encontró i año
        if lista_años[i] == ventas[j][3]:
            # Ir acumulando ventas
            acumulador = acumulador + ventas[j][9]
        # Cambiar registro
        j = j + 1

    # Agregar valor acumulador en una lista
    ventas_años.append(acumulador)
    # Restablecer acumulador
    acumulador = 0
    # Cambiar año a buscar
    i = i + 1

# Imprimir años y sus ventas
i = 0
while i < len(lista_años):
    print(f"{i + 1}. {lista_años[i]} (ventas ${ventas_años[i]})")
    i = i + 1

# Identificar el mayor
mayor_venta = ventas_años[0]
nombre_año = lista_años[0]

i = 0
while i < len(ventas_años):
    if ventas_años[i] > mayor_venta:
        mayor_venta = ventas_años[i]
        nombre_año = lista_años[i]
    i = i + 1

# Validar que no hallan máximos iguales
contador = 0
i = 0 
while i < len(ventas_años):
    if ventas_años[i] == mayor_venta:
        contador = contador + 1
    i = i + 1
print("")

# Si solo hay un máximo
if contador == 1:
    print("Año con más ventas:")
    print(f"{nombre_año} (ventas ${mayor_venta})")
# Si hay varios máximos:
else:
    print("¡Hay máximos iguales!")
    print("Años con mayor ventas: ")
    i = 0
    while i < len(ventas_años):
        if ventas_años[i] == mayor_venta:
            print(f"{lista_años[i]} (ventas ${mayor_venta})")
        i = i + 1

# 5) Mes con mayor ventas
print("- - - -")
print("Meses registrados:")

# Crear una lista de meses
lista_meses = []

# Recorrer registros
i = 0
while i < cantidad_registros:
    # Validar
    if ventas[i][2] not in lista_meses:
        lista_meses.append(ventas[i][2])
    # Cambiar registro
    i = i + 1 

# Contar cada mes registrado
ventas_meses = []
acumulador = 0
i = 0
while i < len(lista_meses):

    # Recorrer registros
    j = 0
    while j < cantidad_registros:
        # Si encontró i mes
        if lista_meses[i] == ventas[j][2]:
            # Ir acumulando ventas
            acumulador = acumulador + ventas[j][9]
        # Cambiar registro
        j = j + 1

    # Agregar valor acumulador en una lista
    ventas_meses.append(acumulador)
    # Restablecer acumulador
    acumulador = 0
    # Cambiar mes a buscar
    i = i + 1

# Imprimir meses y sus ventas
i = 0
while i < len(lista_meses):
    print(f"{i + 1}. {lista_meses[i]} (ventas ${ventas_meses[i]})")
    i = i + 1

# Identificar el mayor
mayor_venta = ventas_meses[0]
nombre_mes = lista_meses[0]

i = 0
while i < len(ventas_meses):
    if ventas_meses[i] > mayor_venta:
        mayor_venta = ventas_meses[i]
        nombre_mes = lista_meses[i]
    i = i + 1

# Validar que no hallan máximos iguales
contador = 0
i = 0 
while i < len(ventas_meses):
    if ventas_meses[i] == mayor_venta:
        contador = contador + 1
    i = i + 1
print("")

# Si solo hay un máximo
if contador == 1:
    print("Mes con más ventas:")
    print(f"{nombre_mes} (ventas ${mayor_venta})")
# Si hay varios máximos:
else:
    print("¡Hay máximos iguales!")
    print("Meses con mayor ventas: ")
    i = 0
    while i < len(ventas_meses):
        if ventas_meses[i] == mayor_venta:
            print(f"{lista_años[i]} (ventas ${mayor_venta})")
        i = i + 1

# 6) Buscar un cliente por cédula
print("- - - -")
cc_buscar = int(input("Ingrese CC a buscar: "))

# Recorrer registros
encontrado = False
i = 0
while i < cantidad_registros:
    # Ir buscando
    if cc_buscar == ventas[i][4]:
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
        if cc_buscar == ventas[i][4]:
            print(f"Nombre: {ventas[i][5]}")
        # Cambiar registro
        i = i + 1