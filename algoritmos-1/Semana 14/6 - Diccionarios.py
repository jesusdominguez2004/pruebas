# 1. Crear diccionario
frutas = {"manzana":5600, "banana":3000, "sandía":3200}

# 2. Preguntar precios con ciclo
while True:
    fruta = input("Ingrese fruta a comprar: ")
    if fruta in frutas:
        kilos = float(input(f"Ingrese kilos de '{fruta}': "))
        total = kilos * frutas[fruta]
        print(f"Total a pagar: ${total}")
    else:
        # 3. Agregar fruta
        menu = input("No existe... ¿Desea agregarla? S/N: ").upper()
        if menu == "S":
            precio_kilo = float(input(f"Ingrese precio kilo de '{fruta}': "))
            frutas[fruta] = precio_kilo
    break

# 4. Imprimir diccionario
print(type(frutas), frutas)