# 1. Importar módulo json
import json

# 2. Crear diccionario
diccionario = {
    "four": ["cuatro", 4],
    "five": 5,
    "two": "dos",
    "one": "uno"
}

# 3. Crear json en txt con with
with open("workData.txt", "w") as archivo:
    json.dump(diccionario, archivo)

# 4. Leer json en txt con with
diccionario = {}
with open("workData.txt", "r") as archivo:
    diccionario = archivo.read()
    print(type(diccionario), diccionario)

    diccionario = json.loads(diccionario)
    print(type(diccionario), diccionario)