# 1. Crear el diccionario
english = {
    "one" : "uno",
    "two" : "dos",
    "three" : "tres",
    "four" : "cuatro",
    "five" :"cinco"
}
print(english, type(english))

# 2. Ingresar palabra a traducir
palabra = input("Ingrese palabra a traducir: ")

# 3. Traducir
if palabra in english: # in keys
    print(english[palabra])
else:
    print(f"'{palabra}' no se ecuentra en nuestra base de datos...")