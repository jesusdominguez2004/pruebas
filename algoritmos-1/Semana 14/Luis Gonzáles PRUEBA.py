# w -> escribir, borra el contenido, crea si no existe.
# a -> escribir al final, no borra el contenido, crea si no existe.
# r -> leer, error si no existe
import json

laptops = {}
print(type(laptops), laptops)

 
print("1. Registrar\n2. Consultar\n3. Editar")
menu = input("¿Qué desea hacer?: ")

if menu == "1":
    while True:
        nombre = input("Ingrese nombre laptop: ")
        referencia = input("Ingrese la referencia")
        precio = float(input("Ingrese el precio: $"))
        marca = input("Ingrese la marca: ")
        color = input("Ingrese el color: ")

        laptops[nombre] = {
            "Referencia": referencia,
            "Precio": precio,
            "Marca": marca,
            "Color": color
        }

        with open("prueba.txt" , "w") as archivo:
            json.dump(laptops, archivo)

        opc = input("¿Desea agregar otra laptop? S/N: ").upper()
        if opc == "N":
            break

if menu == "2":
    print(type(laptops), laptops)
    with open("prueba.txt", "r") as archivo:
        # Obtener json
        diccionario = archivo.read()
        print(type(diccionario), diccionario)

        # Convertir a diccionario
        diccionario = json.loads(diccionario)
        print(type(diccionario), diccionario)

if menu == "3":
    with open("prueba.txt", "r") as archivo:
        # 1. Obtener json de txt
        diccionario = archivo.read()

        # 2. Convertir a diccionario Python
        diccionario = json.loads(diccionario)
        print(type(diccionario), diccionario)

        # 3. Modificarlo de alguna forma
        print("Laptos almacenadas:")
        for i in diccionario:
            print(f"- {i}")

        laptop = input("¿Qué laptop desea modificar?: ")
        if laptop in diccionario:
            print(f"Referencia {laptop}: {diccionario[laptop]['Referencia']}")
            print(f"Precio {laptop}: {diccionario[laptop]['Precio']}")
            print(f"Marca {laptop}: {diccionario[laptop]['Marca']}")
            print(f"Color {laptop}: {diccionario[laptop]['Color']}")
            atributo = input("¿Qué desea cambiar?: ").capitalize()

            if atributo in  diccionario[laptop]:
                if type(diccionario[laptop][atributo]) == float:
                    valor_nuevo = input(f"Ingrese valor nuevo '{atributo}' de laptop '{laptop}': $")
                    diccionario[laptop][atributo] = float(valor_nuevo)
                else:
                    valor_nuevo = input(f"Ingrese valor nuevo '{atributo}' de laptop '{laptop}': ")
                    diccionario[laptop][atributo] = valor_nuevo
            else:
                print(f"{atributo} no es un atributo válido")
        else:
            print(f"{laptop} no está almacenada...")

        print(type(diccionario), diccionario)

        with open("prueba.txt", "w") as archivo:
            # 4. Reemplazar json nuevo a txt 
            json.dump(diccionario, archivo)