# Algortimo "Número mayor y menor"

# Captura de información
num1 = eval(input("Ingrese un primer número: "))
num2 = eval(input("Ingrese un segundo número: "))
num3 = eval(input("Ingrese un tercer número: "))
num4 = eval(input("Ingrese un cuarto número: "))
num5 = eval(input("Ingrese un quinto número: "))

# Iteraciones mayor (Sin usar funciones max or min)

# Iteración 1
if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print("El número mayor es: ", num1)
# Iteración 2
if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("El número mayor es: ", num2)
# Iteración 3
if num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print("El número mayor es: ", num3)   
# Iteración 4
if num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print("El número mayor es: ", num4)
# Iteración 5
if num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
    print("El número mayor es: ", num5)
    
# Iteraciones menor (Sin usar funciones max or min)

# Iteración 6
if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
    print("El número menor es: ", num1)
# Iteración 7
if num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
    print("El número menor es: ", num2)
# Iteración 8
if num3 < num1 and num3 < num2 and num3 <num4 and num3 < num5:
    print("El número menor es: ", num3)   
# Iteración 9
if num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
    print("El número menor es: ", num4)
# Iteración 10
if num5 < num1 and num5 < num2 and num5 < num3 and num5 < num4:
    print("El número menor es: ", num5)