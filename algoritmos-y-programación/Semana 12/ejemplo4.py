# Ejemplo 4:

cantidad = eval(input("Ingrese la cantidad de elementos: "))

miLista = [] # Crear lista...

# Llenar la lista:
for i in range(cantidad): # Range (inicio, fin, step):
    valorLista = eval(input(f"Ingrese un valor para i[{i}]"))
    miLista.append(valorLista) # append() -> agreagar valor al final lista...
print(miLista)

# Sumar los elementos de la lista:
miAcumulador = 0
for i in miLista:
    miAcumulador = miAcumulador + miLista[i-1]
    
# Resultado:
print("Suma de los elementos de miLista[]: ", miAcumulador)