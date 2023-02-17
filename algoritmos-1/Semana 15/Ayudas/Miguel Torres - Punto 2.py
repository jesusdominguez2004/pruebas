# escribir
mi_txt = open("punto2.txt", "w")
mi_txt.write("Barranquilla, Lunes 27, 32 grado..." + "\n")
mi_txt.write("Barranquilla, Martes 28, 29 grado..." + "\n")
mi_txt.write("Barranquilla, Miercoles 29, 30 grado...")
mi_txt.close()

# leer
mi_txt = open("punto2.txt", "r")
info = mi_txt.read()
print(info)
mi_txt.close()

