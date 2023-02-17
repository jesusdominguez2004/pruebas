# Bucle for | Ejemplo 1:

# 1) Variable de control -> [vector]
for i in [1,2,3,4]:
    print(i) # Devolver los elementos de la lista...
    
# 2) Variable de control -> [vector]
for i in [1,1,1,1]:
    print("Hola mundo") # Repetir según la cantidad de elementos de la lista...
    
# 3) Acceder manualmente a una lista:
b = [10, 20, 30, 40, 50]
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])

# 4) función len():
c = [1,2,3,4]
print(c[0]) # Primer elemento de una lista
print(c[len(c) - 1]) # Último elemento de una lista
print(c[0] + c[len(c) - 1]) # Primer elemento + último elemento

# 5) Variable de control -> "Cadena"
for i in "Hola mundo":
    print(i) # Devolver los elementos de la lista...

# 6) Variable de control -> "Cadena"
for i in "Hola mundo":
    if i == "a": # Validación en un ciclo...
        print("Encontré la letra a...")

# 7) Contadores -> Contadores = Contadores + 1:
miContador = 0
for i in "Esta es mi familia":
    if i == "a":
        miContador = miContador + 1
print("Letra a encontrada ", miContador, " veces")  

# 8) Acumuladores -> Acumuladores = Acumuladores + variable:

# 9) Lista estática:
d = ["Manzana", "Peras", "Banana"]
for i in d:
    print(i)
    
# 10) Lista inestática:

# 11) Función range(inicio, fin, incremento):
for i in range(5): # Rango de 0 hasta 4...
    print(i) # Cinco veces...

for i in range(1,11): # Rango de 1 hasta 10...
    print(i) # Diez veces...
    
for i in range(0,11,2): # Rango de 0 hasta 10 con incremento en 2...
    print(i)
