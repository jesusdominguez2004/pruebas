nombre_archivo = 'pronostico.txt'

with open(nombre_archivo, 'w') as f:
    f.write('barranquilla, lunes 27 de abril 35 grados')
    f.write('\n')
    f.write('barranquilla, martes 28 de abril 37 grados')

with open(nombre_archivo, 'r') as f:
    datos = f.read()
    print(datos)
print()

with open(nombre_archivo, 'r') as f:
    for linea in f:
        print(linea, end='')