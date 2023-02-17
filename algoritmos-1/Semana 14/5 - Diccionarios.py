# 1. Crear el diccionario
datosUsuario = {}
print(datosUsuario, type(datosUsuario))

# 2. Llenar diccionario con ciclo
while True:
    x = input("Ingrese key: ")
    datosUsuario[x] = input(f"Ingrese value de '{x}': ")

    menu = input("¿Desea salir? S/N: ").upper()
    if menu == "S":
        break

# 3. Mostrar resultado
print(datosUsuario)