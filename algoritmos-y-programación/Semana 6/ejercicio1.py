# Captura de información
edad = eval(input("Ingrese su edad: "))
# Iteración 1
if edad >= 1 and edad <= 99:
    # Iteración 2
    if edad < 18:
        # Salida
        print("Usted no es mayor de edad, no puede votar...")
        print("Gracias por utilizar nuestros servicios")
    # Iteración 3
    if edad >= 18:
        # Salida
        print("Usted puede votar...")
        print("Gracias por utilizar nuestros servicios")
# Iteración 4      
if edad < 1 or edad > 99:
    # Salida
    print("Edad no válida...")
    print("Gracias por utilizar nuestros servicios")