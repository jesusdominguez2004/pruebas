pares = ["2", "4", "6", "8", "10"]

impares = ["1", "3", "5", "7", "9"]

suma_pares = 0
for i in pares:
    print(i, type(i))
    print(int(i), type(int(i)))
    suma_pares = suma_pares + int(i)
print(suma_pares)

print("")

suma_impares = 0
for i in impares:
    print(i, type(i))
    print(int(i), type(int(i)))
    suma_impares = suma_impares + int(i)
print(suma_impares)