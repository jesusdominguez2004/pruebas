# Ejericio 1

a = []
b = []

cantidad_elementos = eval(input("Ingrese la cantidad de elementos para la lista A y B: "))

# Datos en A:
for i in range(cantidad_elementos):
    elemento = eval(input("Ingrese un elemento para A: "))
    a.append(elemento)

# Datos en B:
for i in range(cantidad_elementos):
    elemento = eval(input("Ingrese un elemento para B: "))
    b.append(elemento)

# Sumar en posiciones iguales:
c = []
for i in range(cantidad_elementos):
    suma_elementos = a[i] + b[i]
    c.append(suma_elementos)

# Imprimir resultados:
print("- - RESULTADOS - -")
print("Lista A: ", a)
print("Lista B: ", b)
print("Lista nueva de sumas de igual posición: ", c) 