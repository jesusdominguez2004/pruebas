# Ejercicio 

# Captura de datos:
localidad = eval(input("Ingrese la localidad del pedido (1, 2, 3 o 4): "))
peso = eval(input("Ingrese el peso del pedido (KG): "))

# Condiciones:
if localidad < 1 or localidad > 4:
    print("Datos ingresados no válidos, selecciones una de las cuatro localidad...")
else:
    if peso <= 0:
        print("Datos ingresados no válidos, peso no válido...")
    else:
        # Localidad 1
        if localidad == 1:
            subTotal = 5000 * peso 
            if peso >= 0.1 and peso < 3:
                descuento = 0.15 # 15%
            elif peso >= 3 and peso < 6:
                descuento = 0.10 # 10%
            elif peso >= 6 and peso < 8:
                descuento = 0.05 # 5%
            elif peso >= 8 and peso < 10:
                descuento = 0.02 # 2%
            elif peso >= 10:
                descuento = 0 # No hay descuento
            total = subTotal - (subTotal * descuento)
            print("- - Resutados - -")
            print("Total: $", total)
            if descuento == 0:
                print("No hay Descuento...")
            else:
                print("Descuento del ", str(descuento * 100) + "%")
        # Localidad 2
        if localidad == 2:
            subTotal = 7500 * peso 
            if peso >= 0.1 and peso < 3:
                descuento = 0.15 # 15%
            elif peso >= 3 and peso < 6:
                descuento = 0.10 # 10%
            elif peso >= 6 and peso < 8:
                descuento = 0.05 # 5%
            elif peso >= 8 and peso < 10:
                descuento = 0.02 # 2%
            elif peso >= 10:
                descuento = 0 # No hay descuento
            total = subTotal - (subTotal * descuento)
            print("- - Resutados - -")
            print("Total: $", total)
            if descuento == 0:
                print("No hay Descuento...")
            else:
                print("Descuento del ", str(descuento * 100) + "%")
        # Localidad 3
        if localidad == 3:
            subTotal = 10000 * peso 
            if peso >= 0.1 and peso < 3:
                descuento = 0.15 # 15%
            elif peso >= 3 and peso < 6:
                descuento = 0.10 # 10%
            elif peso >= 6 and peso < 8:
                descuento = 0.05 # 5%
            elif peso >= 8 and peso < 10:
                descuento = 0.02 # 2%
            elif peso >= 10:
                descuento = 0 # No hay descuento
            total = subTotal - (subTotal * descuento)
            print("- - Resutados - -")
            print("Total: $", total)
            if descuento == 0:
                print("No hay Descuento...")
            else:
                print("Descuento del ", str(descuento * 100) + "%")
        # Localidad 4
        if localidad == 4:
            subTotal = 12500 * peso 
            if peso >= 0.1 and peso < 3:
                descuento = 0.15 # 15%
            elif peso >= 3 and peso < 6:
                descuento = 0.10 # 10%
            elif peso >= 6 and peso < 8:
                descuento = 0.05 # 5%
            elif peso >= 8 and peso < 10:
                descuento = 0.02 # 2%
            elif peso >= 10:
                descuento = 0 # No hay descuento
            total = subTotal - (subTotal * descuento)
            print("- - Resutados - -")
            print("Total: $", total)
            if descuento == 0:
                print("No hay Descuento...")
            else:
                print("Descuento del ", str(descuento * 100) + "%")