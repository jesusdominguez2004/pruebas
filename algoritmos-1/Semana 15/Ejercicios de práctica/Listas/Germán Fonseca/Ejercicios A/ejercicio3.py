# Ejercicio 3 | Tipo A

# Crear listas vacías
codigos = []
usuarios = []
productos = []
totales = []

# Llenar datos
n = int(input("Ingrese número de ventas: "))

i = 0
while i < n:
    codigo = int(input(f"Ingrese el código[{i}]: "))
    usuario = input(f"Ingrese el usuario[{i}]: ").capitalize()
    producto = input(f"Ingrese el producto[{i}] 1. COMPUTADOR, 2. TABLET, 3. CELULAR: ").capitalize()
    
    codigos.append(codigo)
    usuarios.append(usuario)
    
    if producto == "1" or producto == "Computador":
        productos.append("Computador")
        totales.append(500_000)

    elif producto == "2" or producto == "Tablet":
        productos.append("Tablet")
        totales.append(200_000)

    elif producto == "3" or producto == "Celular":
        productos.append("Celular")
        totales.append(100_000)

    else:
        productos.append("N/A")
        totales.append(0)

    print("")
    i = i + 1

# Mostrar datos
i = 0
while i < n:
    print(f"CÓDIGO: {codigos[i]} | USUARIO: {usuarios[i]} | PRODUCTO: {productos[i]} | TOTAL: ${totales[i]}")
    i = i + 1

# 1. Dado un código retornar producto comprado
print("\n1. Dado un código retornar producto comprado")
codigo_buscar = int(input("Ingrese código: "))

if codigo_buscar not in codigos:
    print("Código no encontrado...")
else:
    i = 0
    while i < len(codigos):
        if codigo_buscar == codigos[i]:
            print(f"Producto comprado: {productos[i]}")
            break
        i = i + 1

# 2. Dado un usuario retorne compras que realizó
print("\n2. Dado un usuario retorne compras que realizó")
usuario_buscar = input("Ingrese usuario: ").capitalize()

if usuario_buscar not in usuarios:
    print("Usuario no encontrado...")
else:
    contador = 1
    i = 0
    while i < len(usuarios):
        if usuario_buscar == usuarios[i]:
            print(f"Compra {contador} de {usuario_buscar}: {productos[i]} (${totales[i]})")
            contador = contador + 1
        i = i + 1

# 3. Promedio ventas
print("\n3. Promedio ventas")
acumulador = 0
i = 0
while i < len(totales):
    acumulador = acumulador + totales[i]
    i = i + 1
promedio = acumulador / len(totales)
promedio = round(promedio, 2)
print(f"${promedio}")

# 4. Producto más vendido
print("\n4. Producto más vendido")
computadores = 0
tablets = 0
celulares = 0
na = 0
i = 0
while i < len(productos):
    if productos[i] == "Computador":
        computadores = computadores + 1

    if productos[i] == "Tablet":
        tablets = tablets + 1

    if productos[i] == "Celular":
        celulares = celulares + 1

    i = i + 1

if computadores > tablets and computadores > celulares:
    print(f"¡Computador es el más vendido! ({computadores} compras)")

elif tablets > computadores and tablets > celulares:
    print(f"¡Tablets es el más vendido! ({tablets} compras)")

elif celulares > computadores and celulares > tablets:
    print(f"¡Celulares es el más vendido! ({celulares} compras)")

else:
    print(f"Hay ventas iguales...")
    print(f"Computadores: {computadores}")
    print(f"Tablets: {tablets}")
    print(f"Celulares: {celulares}")


# 5. Dado un producto retorne usuarios compradores
print("\n5. Dado un producto retorne usuarios compradores")
producto_buscar = input("Ingrese producto: ").capitalize()

if producto_buscar not in productos:
    print("Producto no encontrado...")
else:
    i = 0
    while i < len(productos):
        if producto_buscar == productos[i]:
            print(f"- {usuarios[i]}")
        i = i + 1