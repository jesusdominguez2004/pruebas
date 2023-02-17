# Algoritmo "Precio del paquete"

# Captura de información
pesoPaquete = eval(input("Ingrese el peso del paquete (KG): "))

# Iteración 1
if pesoPaquete > 0 and pesoPaquete <= 20:
    # Iteración 2
    if pesoPaquete < 5:
        print("El precio del paquete será: $1500 (Peso ", pesoPaquete, "KG)")
    # Iteración 3
    if pesoPaquete >= 5 and pesoPaquete <= 10:
        print("El precio del paquete será: $2000 (Peso ", pesoPaquete, "KG)")
    # Iteración 4
    if pesoPaquete >= 11 and pesoPaquete <= 20:
        print("El precio del paquete será: $2500 (Peso ", pesoPaquete, "KG)")
# Iteración 5
if pesoPaquete <= 0 or pesoPaquete > 20:
    print("Peso no valido...")