# Prueba de diccionarios

miDiccionario = {
    0:"a", 
    1:"b", 
    2:"c"
}

print(miDiccionario.get(0)) # return "a"
print(miDiccionario.get(1)) # return "b"
print(miDiccionario.get(2)) # return "c"

# Agregar más key:values

# miDiccionario[key_nuevo] = value
miDiccionario[3] = "d"
miDiccionario[4] = "e"
miDiccionario[5] = "f"

print(miDiccionario.get(3)) # return "d"
print(miDiccionario.get(4)) # return "e"
print(miDiccionario.get(5)) # return "f"


miDiccionario = {
    0: {"a", "b", "c"}, 
    1: {"a", "b", "c"}, 
    2: {"a", "b", "c"}
}
final = "c"
conjunto = miDiccionario.get(0)
print(conjunto)
if final in conjunto:
    print(f"{final} está en {conjunto}")

llave = 0
for x in miDiccionario[llave]:
    print(f"{llave} - {x}")

for llave in miDiccionario:
    for x in miDiccionario[llave]:
        print(f"{llave} - {x}")