# Si una persona puede votar | Ejemplo 3:

cantidadPersonas = eval(input("Ingrese la cantidad de personas: "))

# Mi contador
miContador = 0
# Ciclo
for i in range(1,cantidadPersonas + 1,1):
    miContador = miContador + 1
    edad = eval(input(f"Ingrese la edad de la persona número {miContador}")) 
    # Validar su edad:
    if edad >= 18:
        print("La persona número ", miContador, " puede votar...")
    else:
        print("La persona número ", miContador, " no puede votar...")
