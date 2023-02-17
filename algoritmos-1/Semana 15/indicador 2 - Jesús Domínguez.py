# INDICADOR 2: almacenar y leer datos históricos acerca del pronóstico del tiempo de una determinada ciudad.

# 1. Crear y escribir
with open("2 - Pronóstico.txt", "w", encoding="utf-8") as file:
    file.write("Barranquilla, Lunes 19 de Abril 35 grados\n")
    file.write("Barranquilla, Martes 20 de Abril 37 grados\n")
    file.write("Barranquilla, Miércoles 21 de Abril 38 grados")

# 2. Leer
with open("2 - Pronóstico.txt", "r", encoding="utf-8") as file:
    contenido = file.read()
    print(contenido)