# ARCHIVOS DE FORMA DINÁMICA (MEJORADO)
from colorama import Fore, Back, Style, init
init(autoreset=True)

# 1. Nombre archivos
nombre_archivos = ["ventas_enero.txt", "ventas_febrero.txt"]

# 2. Directorio
path = "Archivos/"

# 3. Generar rutas
for i in nombre_archivos:
    archivo = path + i

    # 4. Lista de cada línea
    informacion = open(archivo, "r+")
    lista_elementos = []
    for j in informacion:
        lista_elementos.append(int(j))
    print(f"Lista de {Fore.GREEN + Style.BRIGHT + i + Fore.RESET + Style.RESET_ALL}: {lista_elementos}")

    # 5. Promedio, mayor y menor
    contador = 0
    acumulador = 0
    mayor = lista_elementos[0]
    menor = lista_elementos[0]
    for k in lista_elementos:
        acumulador = acumulador + k
        contador = contador + 1
        if k > mayor:
            mayor = k
        if k < menor:
            menor = k
    promedio = round(acumulador / contador, 2)

    print(f"Promedio {Fore.GREEN + Style.BRIGHT + i + Fore.RESET + Style.RESET_ALL}: ${promedio}")
    print(f"Mayor {Fore.GREEN + Style.BRIGHT + i + Fore.RESET + Style.RESET_ALL}: ${mayor}")
    print(f"Menor {Fore.GREEN + Style.BRIGHT + i + Fore.RESET + Style.RESET_ALL}: ${menor}")
    print(f"Cantidad elementos {Fore.GREEN + Style.BRIGHT + i + Fore.RESET + Style.RESET_ALL}: {contador}")

    # 6. Valores mayores y menores a x
    x = int(input("Ingrese un número: $"))
    for l in lista_elementos:
        if l > x:
            print(f"{Fore.BLUE + '$' + str(l) + Fore.RESET + Style.RESET_ALL} es mayor que ${x}")
        if l < x:
            print(f"{Fore.RED + '$' + str(l) + Fore.RESET + Style.RESET_ALL} es menor que ${x}")
        if l == x:
            print(f"{Fore.YELLOW + '$' + str(l) + Fore.RESET + Style.RESET_ALL} es igual que ${x}")

    # 7. Devolver veces encontrado un número
    y = int(input(f"Ingrese un número a buscar en {i}: "))
    veces = 0
    for m in lista_elementos:
        if y == m:
            veces = veces + 1
    print(f"Veces encontrado en {i}: {veces}")
    print("")