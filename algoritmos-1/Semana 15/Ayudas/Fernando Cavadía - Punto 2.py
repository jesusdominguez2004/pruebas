# crear y escribir en el archivo pronostico.txt
n = int(input('¿Cuántos pronosticos quiere agregar?: '))

archivo = open('pronostico.txt', 'w')
for x in range(n):
    city = input(f'Ingrese la ciudad {x + 1}: ')
    date = input(f'Ingrese la fecha {x + 1}: ')
    temp = input(f'Ingrese la temperatura {x + 1}: ')
    archivo.write(f'{city}, {date}, temperatura de {temp} grados' + '\n')
archivo.close()

archivo = open('pronostico.txt', 'r')
print(archivo.read())
archivo.close()