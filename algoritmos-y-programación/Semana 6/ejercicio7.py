# Algoritmo "Par o impar"

# Captura de información
num = eval(input("Ingrese un número: "))

# Iteración 1
if num != 0:
    # Iteración 2
    if num % 2 == 0:
        print(num, " es un número par")
    # Iteración 3
    if num % 2 != 0:
        print(num, " es un número impar")
# Iteración 3
if num == 0:
    print("0 es un número neutro")