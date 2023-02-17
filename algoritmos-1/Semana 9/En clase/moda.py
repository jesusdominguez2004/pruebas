# Moda de un vector | 1.0

a = [10, 10, 20, 20, 30]

# Cuando es una sola moda
moda = a[0]
contadorMayor = 0

for i in range(len(a)):
    contador = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            contador = contador + 1
    if contador > contadorMayor:
        moda = a[i]
        contadorMayor = contador

print(moda)