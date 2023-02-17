#lectura de archivos

datos=["ventas_enero.txt","ventas_febrero.txt"]

path="txt/"
cont=0
acumulador=0
cont2=0
for i in datos:
    cont=cont+1
    archivo=path+i
    informacion=open(archivo,"r+")
    #print("Archivo "+str(cont))
    linea0=informacion.readline()
    mayor=int(linea0)
    menor=int(linea0)
    informacion=open(archivo,"r+")
    for j in informacion:
        if int(j) > mayor:
            mayor=int(j)
        if int(j) < menor:
            menor=int(j)
        acumulador=acumulador+int(j)
        cont2=cont2+1
    promedio=acumulador/cont2
    print("Promedio "+ "Archivo " + str(cont)+ "= "+str(promedio))
    print("Mayor Elemento del  "+ "Archivo " + str(cont)+ "= "+str(mayor))
    print("Menor Elemento del  "+ "Archivo " + str(cont)+ "= "+str(menor))
