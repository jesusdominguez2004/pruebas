# Algoritmo "Ventas accesorio celulares"

# Captura de información
print("- - - Menú - - -")
print("1) Carcasas")
print("2) Cargador")
print("3) Audífonos")
producto = eval(input("Ingrese el tipo de producto: "))

# Iteración 1
if producto >= 1 and producto <= 3:
    # Iteración 2
    if producto == 1:
        cantidad = eval(input("Ingrese su cantidad: "))
        # Iteración 3
        if cantidad >= 1:
            precio = cantidad * 25000
            print("Valor a pagar: $", precio, " (Carcasas)")
        # Iteración 4
        if cantidad < 1:
            print("Cantidad no valida...")
    # Iteración 5
    if producto == 2:
        cantidad = eval(input("Ingrese su cantidad: "))
        # Iteración 6
        if cantidad >= 1:
            precio = cantidad * 10000
            print("Valor a pagar: $", precio, " (Cargador)")
        # Iteración 7
        if cantidad < 1:
            print("Cantidad no valida...")
    # Iteración 8
    if producto == 3:
        cantidad = eval(input("Ingrese su cantidad: "))
        # Iteración 9
        if cantidad >= 1:
            precio = cantidad * 35000
            print("Valor a pagar: $", precio, " (Audífonos)")
        # Iteración 10
        if cantidad < 1:
            print("Cantidad no valida...")
            
# Iteración 11
if producto < 1 or producto > 3:
    print("Tipo de producto no valido...")
        