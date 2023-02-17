# Ejercicio 1 | Vectores | Jesús Domínguez

# Cantidad de elementos:
cantidad = eval(input("Ingrese la cantidad de elementos: "))

# Definir listas:
a = [] # Usuario
b = [] # Usuario
c = [] # Sistema
d = [] # Usuario
e = [] # Sistema
f = [] # Usuario
g = [] # Sistema

# Llenar lista a:
i = 0
while i < cantidad:
    elemento = eval(input(f"Ingrese el elemento a[{i}]: "))
    a.append(elemento)
    i = i + 1

# Llenar lista b:
i = 0
while i < cantidad:
    elemento = eval(input(f"Ingrese el elemento b[{i}]: "))
    b.append(elemento)
    i = i + 1

# Llenar lista c:
i = 0
while i < cantidad:
    # c = a + b
    elemento = a[i] + b[i]
    c.append(elemento)
    i = i + 1

# Llenar lista d:
i = 0
while i < cantidad:
    elemento = eval(input(f"Ingrese el elemento d[{i}]: "))
    d.append(elemento)
    i = i + 1

# Llenar lista e:
i = 0
while i < cantidad:
    # e = c + d invertida
    elemento = c[i] + d[cantidad - 1 - i]
    e.append(elemento)
    i = i + 1

# Llenar lista f:
i = 0
while i < cantidad:
    elemento = eval(input(f"Ingrese el elemento f[{i}]: "))
    f.append(elemento)
    i = i + 1

# Llenar lista g:
i = 0
while i < cantidad:
    # g = e ** f, invertir también
    elemento = e[cantidad - 1 - i] ** f[cantidad - 1 - i]
    g.append(elemento)
    i = i + 1

# Resultados:
print("- - RESULTADOS - -")
print("Lista a:", a)
print("Lista b:", b)
print("Lista c:", c)
print("Lista d:", d)
print("Lista e:", e)
print("Lista f:", f)
print("Lista g:", g)