# Cantidad de elementos
n = eval(input("Ingrese cantidad de elementos: "))

a = []

for i in range(n):
    elemento = eval(input(f"Ingrese elemento a[{i}]: "))
    a.append(elemento)

print(a)

# Invertir a con For
for i in range(len(a) - 1, - 1, -1):
    print(a[i])

# Invertir a con While (1)
i = len(a) - 1
while i >= 0:
    print(a[i])
    i = i - 1