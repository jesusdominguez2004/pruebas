"""
r  -> Leer, si no existe error
r+ -> Leer y escribir, si no existe error
w  -> Escribir borra la información existente, si no existe lo crea
a  -> Añadir información sin borrar, si no existe lo crea
a+ -> Añadir y leer información sin borrar, si no existe lo cre

t  -> Modo texto
b  -> Modo binario
"""

# 1. Lectura del archivo
informacion = open("Archivos/nombres.txt", "r+")
for i in informacion:
    print(i)

# 2. Escritura en el archivo
informacion.write("\nUna linea al final (r+)")

# 3. Cerrar para guardar
informacion.close()