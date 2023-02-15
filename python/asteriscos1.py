# Dibujar números | Asteriscos

# Leer número:
numero = input("Ingrese un número entero positivo: ")

# Validar:
while numero.isnumeric() == False:
    print("Datos ingresados no válidos...")
    numero = input("Ingrese un número entero positivo: ")

print("- - RESULTADO - -")

# - - Dibujar - -

# Fila 1:
for i in range(len(numero)):
    if numero[i] == "0":
        print("  * *  ", end="  ")
    elif numero[i] == "1":
        print("    *  ", end="  ")
    elif numero[i] == "2":
        print("  * *  ", end="  ")
    elif numero[i] == "3":
        print("  * *  ", end="  ")
    elif numero[i] == "4":
        print("*     *", end="  ")
    elif numero[i] == "5":
        print("* * * *", end="  ")
    elif numero[i] == "6":
        print("  * *  ", end="  ")
    elif numero[i] == "7":
        print("* * * *", end="  ")
    elif numero[i] == "8":
        print("  * *  ", end="  ")
    elif numero[i] == "9":
        print("  * *  ", end="  ")

print("")

# Fila 2:
for i in range(len(numero)):
    if numero[i] == "0":
        print("*     *", end="  ")
    elif numero[i] == "1":
        print("  * *  ", end="  ")
    elif numero[i] == "2":
        print("*     *", end="  ")
    elif numero[i] == "3":
        print("*     *", end="  ")
    elif numero[i] == "4":
        print("*     *", end="  ")
    elif numero[i] == "5":
        print("*      ", end="  ")
    elif numero[i] == "6":
        print("*     *", end="  ")
    elif numero[i] == "7":
        print("      *", end="  ")
    elif numero[i] == "8":
        print("*     *", end="  ")
    elif numero[i] == "9":
        print("*     *", end="  ")

print("")

# Fila 3:
for i in range(len(numero)):
    if numero[i] == "0":
        print("*     *", end="  ")
    elif numero[i] == "1":
        print("    *  ", end="  ")
    elif numero[i] == "2":
        print("      *", end="  ")
    elif numero[i] == "3":
        print("      *", end="  ")
    elif numero[i] == "4":
        print("*     *", end="  ")
    elif numero[i] == "5":
        print("* * *  ", end="  ")
    elif numero[i] == "6":
        print("*      ", end="  ")
    elif numero[i] == "7":
        print("      *", end="  ")
    elif numero[i] == "8":
        print("*     *", end="  ")
    elif numero[i] == "9":
        print("*     *", end="  ")

print("")

# Fila 4:
for i in range(len(numero)):
    if numero[i] == "0":
        print("*     *", end="  ")
    elif numero[i] == "1":
        print("    *  ", end="  ")
    elif numero[i] == "2":
        print("    *  ", end="  ")
    elif numero[i] == "3":
        print("  * *  ", end="  ")
    elif numero[i] == "4":
        print("  * * *", end="  ")
    elif numero[i] == "5":
        print("      *", end="  ")
    elif numero[i] == "6":
        print("* * *  ", end="  ")
    elif numero[i] == "7":
        print("    *  ", end="  ")
    elif numero[i] == "8":
        print("  * *  ", end="  ")
    elif numero[i] == "9":
        print("  * * *", end="  ")

print("")

# Fila 5:
for i in range(len(numero)):
    if numero[i] == "0":
        print("*     *", end="  ")
    elif numero[i] == "1":
        print("    *  ", end="  ")
    elif numero[i] == "2":
        print("  *    ", end="  ")
    elif numero[i] == "3":
        print("      *", end="  ")
    elif numero[i] == "4":
        print("      *", end="  ")
    elif numero[i] == "5":
        print("      *", end="  ")
    elif numero[i] == "6":
        print("*     *", end="  ")
    elif numero[i] == "7":
        print("    *  ", end="  ")
    elif numero[i] == "8":
        print("*     *", end="  ")
    elif numero[i] == "9":
        print("      *", end="  ")

print("")

# Fila 6:
for i in range(len(numero)):
    if numero[i] == "0":
        print("*     *", end="  ")
    elif numero[i] == "1":
        print("    *  ", end="  ")
    elif numero[i] == "2":
        print("*      ", end="  ")
    elif numero[i] == "3":
        print("*     *", end="  ")
    elif numero[i] == "4":
        print("      *", end="  ")
    elif numero[i] == "5":
        print("*     *", end="  ")
    elif numero[i] == "6":
        print("*     *", end="  ")
    elif numero[i] == "7":
        print("  *    ", end="  ")
    elif numero[i] == "8":
        print("*     *", end="  ")
    elif numero[i] == "9":
        print("*     *", end="  ")

print("")

# Fila 7:
for i in range(len(numero)):
    if numero[i] == "0":
        print("  * *  ", end="  ")
    elif numero[i] == "1":
        print("  * * *", end="  ")
    elif numero[i] == "2":
        print("* * * *", end="  ")
    elif numero[i] == "3":
        print("  * *  ", end="  ")
    elif numero[i] == "4":
        print("      *", end="  ")
    elif numero[i] == "5":
        print("  * *  ", end="  ")
    elif numero[i] == "6":
        print("  * *  ", end="  ")
    elif numero[i] == "7":
        print("  *    ", end="  ")
    elif numero[i] == "8":
        print("  * *  ", end="  ")
    elif numero[i] == "9":
        print("  * *  ", end="  ")