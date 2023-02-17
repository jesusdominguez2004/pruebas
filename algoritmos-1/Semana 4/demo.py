# Ejercicio 1 | Semana 4 | Algoritmos 1
 
# Crear matriz
ventas = [] 

# Cantidad de registros
cantidad_registros = int(input("Ingrese la cantidad de registros: "))
print("- - - -")

# Llenar matriz
i = 0
while i < cantidad_registros:
    # Agregar fila en blanco
    ventas.append([])

    # Ingresar datos
    dia = int(input(f"Ingrese el día (Cliente {i+1}): "))
    mes = int(input(f"Ingrese el mes (Cliente {i+1}): "))
    ano = int(input(f"Ingrese el año (Cliente {i+1}): "))
    cc = int(input(f"Ingrese la CC (Cliente {i+1}): "))
    nombre_cliente = input(f"Ingrese el nombre cliente (Cliente {i+1}): ")

    producto = input(f"Ingrese el producto (Cliente {i+1}): ")
    cantidad = int(input(f"Ingrese la cantidad (Cliente {i+1}): "))
    valor_unitario = int(input(f"Ingrese el valor unitario (Cliente {i+1}): "))
    total = cantidad * valor_unitario
    print("- - - -")

    # Almacenar datos
    ventas[i].append(i + 1)
    ventas[i].append(dia)
    ventas[i].append(mes)
    ventas[i].append(ano)
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
print(f"Total de ventas: {total_ventas}")

# 2) Calcule el producto más vendido
print("- - - -")
print("Productos vendidos:")

# Crear una lista de productos
lista_productos = []

# Recorrer registros
i = 0
while i < cantidad_registros:
    # Validar
    if ventas[i][6] not in lista_productos:
        lista_productos.append(ventas[i][6])
    # Cambiar registro
    i = i + 1 

contador = 0 # contador de veces encontrado
lista_contadores = [] # lista con los valores finales de n

# Recorrer lista producto
i = 0
while i < len(lista_productos):

    # Recorrer registros
    j = 0
    while j < cantidad_registros:
        # Buscar producto...
        if lista_productos[i] == ventas[j][6]:
            # Ir contando...
            contador = contador + 1 
        # Cambiar registro
        j = j + 1

    # Guardar valor de contador
    lista_contadores.append(contador)
    # Restablecer contador
    contador = 0
    # Cambiar palabra a buscar
    i = i + 1

# Imprimir resultados
i = 0
while i < len(lista_productos):
    print(f"{lista_productos[i]}: {lista_contadores[i]}")
    i = i + 1

# Cuál es mayor
producto_mas_vendido = lista_contadores[0]
nombre_producto = lista_productos[0]

# Recorrer lista contadores
i = 0
while i < len(lista_contadores):
    # Encontrar el contador mayor
    if lista_contadores[i] > producto_mas_vendido:
        producto_mas_vendido = lista_contadores[i]
        nombre_producto = lista_productos[i]
    # Cambiar contador
    i = i + 1

print(f"Producto más vendido: {nombre_producto} ({producto_mas_vendido})")

# 3) Calcule el promedio de ventas en un mes y año especificado
print("- - - -")
ano_buscar = int(input("Ingrese año a buscar: "))
mes_buscar = int(input("Ingrese mes a buscar:"))

acumulador = 0
contador = 0
# Recorrer registros
i = 0
while i < cantidad_registros:

    # Si año_buscar == año_registrado... and Si mes_buscar == mes_registrado...
    if ano_buscar == ventas[i][3] and mes_buscar == ventas[i][2]:
        # Ir acumulando
        acumulador = acumulador + ventas[i][9]
        contador = contador + 1
    # Cambiar registro
    i = i + 1

# Dividir
if contador != 0:
    promedio = acumulador / contador
    print(f"Promedio ventas de año {ano_buscar} mes {mes_buscar}: {promedio}")
else:
    print(f"Promedio ventas de año {ano_buscar} mes {mes_buscar}: 0")

# 4) Año con mayor ventas
print("- - - -")

# Crear una lista de años
lista_anos = []

i = 0
while i < cantidad_registros:
    # Validar
    if ventas[i][3] not in lista_anos:
        lista_anos.append(ventas[i][3])
    # Cambiar registro
    i = i + 1 

# Escoger año
n = 0
m = []
i = 0
while i < len(lista_anos):
    # Buscar año
    j = 0
    while j < cantidad_registros:
        # Si coincide...
        if lista_anos[i] == ventas[j][3]:
            n = n + ventas[j][9]
        # Cambiar registro
        j = j + 1

    m.append(n)
    n = 0
    # Cambiar palabra a buscar
    i = i + 1

# Imprimir resultados
i = 0
while i < len(lista_anos):
    print(f"Total ventas año {lista_anos[i]}: ${m[i]}")
    i = i + 1

# Cuál es mayor
ano_mayor = m[0]
nombre_ano = lista_anos[0]
x = 0

# Recorrer años
i = 0
while i < len(lista_anos):

    # Ventas de i años > año mayor...
    if m[i] > ano_mayor:
        ano_mayor = m[i]
        nombre_ano = lista_anos[i]

    # Cambiar año
    i = i + 1

# Imprimir resultados
print(f"Año con más ventas: {nombre_ano} (${ano_mayor})")

# 5) Mes con mayor ventas
print("- - - -")

# Crear una lista de mes
lista_meses = []

i = 0
while i < cantidad_registros:
    # Validar
    if ventas[i][2] not in lista_meses:
        lista_meses.append(ventas[i][2])
    # Cambiar registro
    i = i + 1 

# Escoger mes
n = 0
m = []
i = 0
while i < len(lista_meses):
    # Buscar mes
    j = 0
    while j < cantidad_registros:
        # Si coincide...
        if lista_meses[i] == ventas[j][2]:
            n = n + ventas[j][9]
        # Cambiar registro
        j = j + 1

    m.append(n)
    n = 0
    # Cambiar palabra a buscar
    i = i + 1

# Imprimir resultados
i = 0
while i < len(lista_meses):
    print(f"Total ventas mes {lista_meses[i]}: ${m[i]}")
    i = i + 1

# Cuál es mayor
mes_mayor = m[0]
nombre_mes = lista_meses[0]
x = 0

# Recorrer mes
i = 0
while i < len(lista_meses):

    # Ventas de i mes > mes mayor...
    if m[i] > mes_mayor:
        mes_mayor = m[i]
        nombre_mes = lista_meses[i]

    # Cambiar mes
    i = i + 1

# Imprimir resultados
print(f"Mes con más ventas: {nombre_mes} (${mes_mayor})")

# 6) Buscar un cliente por cédula
print("- - - -")
cc_buscar = int(input("Ingrese CC a buscar:"))

# Recorrer registros
i = 0
while i < cantidad_registros:

    if cc_buscar == ventas[i][4]:
        encontrado = True
    
    # Cambiar registro
    i = i + 1