# 1. Importar módulo json
import json

# 2. Crear diccionario
agenda = {}
print(agenda, type(agenda))

# 3. Llenar diccionario con ciclo
while True:
    documento = input("Ingrese documento: ")
    nombre = input("Ingrese nombre: ")
    telefono = input("Ingrese telefono: ")
    correo = input("Ingrese correo: ")
    
    # Clasificar por documentos
    agenda[documento] = {
        "Nombre" : nombre,
        "Teléfono" : telefono,
        "Correo" : correo
    }

    menu = input("¿Desea agregar otro contacto? S/N: ").upper()
    if menu == "N":
        break

# 4. Imprimir diccionario
print(type(agenda), agenda)

# 5. Convertir a un JSON
print("json.dumps(diccionario)\njson.dump(diccionario, archivo)")
x = json.dumps(agenda)
print(type(x), x)

# 6. JSON a un archivo
archivo = open("agenda.txt", "w")
json.dump(agenda, archivo)
archivo.close()
agenda.clear()

# 7. Leer JSON de un archivo txt
archivo = open("agenda.txt", "r")
agenda = archivo.read()
print(type(agenda), agenda)
archivo.close()