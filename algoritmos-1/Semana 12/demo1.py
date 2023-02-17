# Crear archivo txt ("archivo.txt", "w")
try:
    archivo = open("demo1.txt", "w")
except:
    print("Archivo no existe, archivo creado...")

# Anexar a su información ("archivo.txt", "a")
try:
    archivo = open("demo1.txt", "a")
    archivo.write("Hola mundo")
    archivo.write("\nHola 123")
    archivo.close()
except:
    print("Archivo no existe, archivo creado...")

# Leer su información ("archivo.txt", "r")
try:
    archivo = open("demo1.txt", "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()
except:
    print("Archivo no existe...") 