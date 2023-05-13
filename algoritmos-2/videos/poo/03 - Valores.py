# Valores | 03

# Tipo valor esperado
def sumar(num1: int, num2: int):
    print(f"{num1} + {num2} = {num1 + num2}")

sumar(30, 2) # Llamado 1
sumar(70, 3) # Llamado 2
sumar(10, 5) # Llamado 3

print("")

# Tipo valor regresado
def sumar(num1: int, num2: int) -> str:
    print(f"{num1} + {num2} = {num1 + num2}")

sumar(30.5, 2) # Llamado 1
sumar(70, 3) # Llamado 2
sumar(10, 5) # Llamado 3
