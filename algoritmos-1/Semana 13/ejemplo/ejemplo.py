# creamos variable para la lectura del archivo txt
informacion=open("txt/datos.txt","r+")

for i in informacion:
    print(i)

#escritura
informacion.write("\n"+"agregando una linea al final")
informacion.close()
