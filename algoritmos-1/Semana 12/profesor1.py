import os
os.system("cls")
# creacion archivo
# try:
#     archivo = open("notas.txt", "w")
#     archivo.close()
# except:
#     print("El archivo no existe")

# anexar informacion
# try:
#     archivo = open("notas.txt", "a")
#     # archivo.write("Hola mundo")
#     archivo.write("\nhola 2000")
#     archivo.close()
# except:
#     print("no existe ese archivo")    

try:
    archivo = open("notas.txt", "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()
except:
    print("no existe ese archivo")    