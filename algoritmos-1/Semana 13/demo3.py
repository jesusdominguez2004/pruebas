# FORMA 1
archivo_1 = open("Archivos/ventas_enero.txt", "r+")
lista = archivo_1.readlines()
print(lista)
x = int(lista[0]) + int(lista[1])
print(x)

# FORMA 2
archivo_1 = open("Archivos/ventas_enero.txt", "r+")
lista = []
for i in archivo_1:
    lista.append(int(i)) 
print(lista)

x = lista[0] + lista[1]
print(x)