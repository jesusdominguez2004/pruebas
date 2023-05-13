# Primero conceptos diccionarios

lista = ["abc", 123, 3.1416, 2j, True, False, None, [123, 456]]
tupla = ("abc", 123, 3.1416, 2j, True, False, None, [123, 456])
set = {"abc", 123, 3.1416, 2j, True, False, None}

print(type(lista), lista)
print(type(tupla), tupla)
print(type(set), set)

diccionario = {"a": 0, "b": 1, "c": 2}
diccionario = {
    "a": 0, 
    "b": 1, 
    "c": 2
}
print(type(diccionario), diccionario)


diccionario = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
diccionario = {
    "a": [1, 2, 3], 
    "b": [4, 5, 6], 
    "c": [7, 8, 9]
}
print(type(diccionario), diccionario)

diccionario = {"color": "azul", "modelo": 2019, "placa": "ABC123"}
diccionario = {
    "color": "azul", 
    "modelo": 2019, 
    "placa": "ABC123"
}
print(type(diccionario), diccionario)


# Cómo obtener todas las keys (llaves)
print(diccionario.keys())

llaves = diccionario.keys()
print(llaves)

print(list(diccionario.keys()))

llaves = list(diccionario.keys())
print(llaves)

# Cómo obtener todas los value (valores)
print(diccionario.values())

values = diccionario.values()
print(values)

print(list(diccionario.values()))

values = list(diccionario.values())
print(values)

# Cómo obtener todas los items (key:values)
print(diccionario.items())

items = diccionario.items()
print(items)

print(list(diccionario.items()))

items = list(diccionario.items())
print(items)


# Recorrer llaves diccionario con un for
for llaves in diccionario:
    print(llaves)

for llaves in diccionario.keys():
    print(llaves)

# Recorrer values diccionario con un for
for values in diccionario.values():
    print(values)


# Cómo añadir un item (key:value)
diccionario = {
    "color": "azul", 
    "modelo": 2019, 
    "placa": "ABC123"
}

diccionario["llantas"] = 4
print(type(diccionario), diccionario)

# Cómo actualizar un item (key:value)
diccionario = {
    "color": "azul", 
    "modelo": 2019, 
    "placa": "ABC123",
    "llantas": 4
}

diccionario["color"] = "rojo"
print(type(diccionario), diccionario)

# Cómo borrar un key
diccionario = {
    "color": "rojo", 
    "modelo": 2019, 
    "placa": "ABC123",
    "llantas": 4
}
diccionario.pop("llantas")
print(type(diccionario), diccionario)

# Contar keys
diccionario = {
    "color": "rojo", 
    "modelo": 2019, 
    "placa": "ABC123",
    "llantas": 4
}
print(diccionario)
print(len(diccionario))
print(len(diccionario.keys()))


# Cómo obtener value de un key ingresado
diccionario = {
    "color": "rojo", 
    "modelo": 2019, 
    "placa": "ABC123",
    "llantas": 4
}

print(diccionario.get("modelo"))

