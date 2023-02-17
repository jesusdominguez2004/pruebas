# Ejercicio 3 | Vectores final | Jesús Domínguez

# Definir listas:
nombres = ["Fabio", "Pedro", "Carlos", "Juan"]
producto = ["Arroz", "Carne", "Arroz", "Sopa"]
valor = [12000, 15000, 12000, 8000]
cantidad = [2, 3, 1, 5]
total = [24000, 45000, 12000, 40000]

# 1) Ingresar nombre:
nombre_ingresado = input("Ingrese el nombre del usuario: ")

i = 0
while i < len(nombres):
    # Buscar usuario + sus datos
    if nombre_ingresado == nombres[i]:
        print("- - RESULTADOS - -")
        print("1) Detalles de la compra de", nombre_ingresado, ":")
        print("Producto de", nombre_ingresado, ":", producto[i])
        print("Valor producto de", nombre_ingresado, ": $", valor[i])
        print("Cantidad de", nombre_ingresado, ":", cantidad[i])
        print("Total de", nombre_ingresado, ": $", total[i])
    i = i + 1

# 2) Total ingresos generados:
total_ingresos = 0
i = 0
while i < len(total):
    total_ingresos = total_ingresos + total[i]
    i = i + 1
print("2) Total ingresos: $", total_ingresos)

# 3) Valor mayor dentro del total:
total_mayor = total[0]
i = 0
while i < len(total):
    if total[i] > total_mayor:
        total_mayor = total[i]
    i = i + 1
print("3) Total mayor: $", total_mayor)

# 4) Dado un producto mostrar los clientes que lo compraron:
producto_ingresado = input("Ingrese el producto: ")
 
print("4) Clientes que compraron", producto_ingresado, ":")

i = 0
while i < len(producto):
    # Buscar producto
    if producto_ingresado == producto[i]:
        # Devolver su comprador:
        print(nombres[i])
    i = i + 1