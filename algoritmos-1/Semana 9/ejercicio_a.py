# Ejercicio A | Semana 9 | Jesús Domínguez

# ID | NOMBRE | TIPO DOC | NUM DOC | PRODUCTO | CANTIDAD | VALOR | TOTAL
# 1) Total ventas
# 2) Producto más vendido
# 3) Búsqueda por ID

# Clase ventas
class Ventas():
    def __init__(self):
        self.__ventas = []

    def setVentas(self, x:list):
        self.__ventas = x

    def getVentas(self):
        return self.__ventas

    def llenarDatos(self):
        print("")
        print("LLENAR DATOS")
        filas = int(input("Ingrese la cantidad de filas: "))
        for i in range(filas):
            self.getVentas().append([])
            for j in range(8):
                if j == 0:
                    id = int(input(f"Ingrese ID cliente {i + 1}: "))
                    self.getVentas()[i].append(id)
                if j == 1:
                    nombre = input(f"Ingrese NOMBRE cliente {i + 1}: ")
                    self.getVentas()[i].append(nombre)
                if j == 2:
                    tipoDocumento = input(f"Ingrese TIPO DOCUMENTO cliente {i + 1}: ")
                    self.getVentas()[i].append(tipoDocumento)
                if j == 3:
                    numDocumento = input(f"Ingrese NUMÉRO DOCUMENTO cliente {i + 1}: ")
                    self.getVentas()[i].append(numDocumento)
                if j == 4:
                    producto = input(f"Ingrese PRODUCTO cliente {i + 1}: ")
                    self.getVentas()[i].append(producto)
                if j == 5:
                    cantidad = int(input(f"Ingrese CANTIDAD cliente {i + 1}: "))
                    self.getVentas()[i].append(cantidad)
                if j == 6:
                    valor = int(input(f"Ingrese VALOR cliente {i + 1}: "))
                    self.getVentas()[i].append(valor)
                if j == 7:
                    total = valor * cantidad
                    self.getVentas()[i].append(total)
            print("")

    def mostrarDatos(self):
        print("MOSTRAR DATOS")
        # print(self.getVentas())
        for i in range(len(self.getVentas())):
            print(f"{i+1}. ID: {self.getVentas()[i][0]} | NOMBRE: {self.getVentas()[i][1]} | TIPO DOC: {self.getVentas()[i][2]} | NUM DOC: {self.getVentas()[i][3]} | PRODUCTO: {self.getVentas()[i][4]} | CANTIDAD: {self.getVentas()[i][5]} | VALOR: ${self.getVentas()[i][6]} | TOTAL: ${self.getVentas()[i][7]}")

    def totalVentas(self):
        print("")
        print("TOTAL VENTAS")
        total_ventas = 0
        for i in range(len(self.getVentas())):
            total_ventas = total_ventas + self.getVentas()[i][7]
        print(f"${total_ventas}")

    def productoMasVendido(self):
        print("")
        print("PRODUCTO MÁS VENDIDO")
        # 1. Lista de productos sin repetir
        lista_productos = []
        for i in range(len(self.getVentas())):
            if self.getVentas()[i][1] not in lista_productos:
                lista_productos.append(self.getVentas()[i][4])

        # 2. Lista de contadores productos
        conteo_productos = []
        contador = 0
        for i in range(len(lista_productos)):
            for j in range(len(self.getVentas())):
                if lista_productos[i] == self.getVentas()[j][4]:
                    contador = contador + self.getVentas()[j][5] # Cantidad
            conteo_productos.append(contador)
            contador = 0
        
        # 3. Mostrar productos y sus cantidades
        for i in range(len(lista_productos)):
            print(f"{lista_productos[i]} (cantidad {conteo_productos[i]})")

        # 4. Contador mayor
        mayor = conteo_productos[0]
        nombre_producto = lista_productos[0]
        for i in range(len(lista_productos)):
            if conteo_productos[i] > mayor:
                mayor = conteo_productos[i]
                nombre_producto = lista_productos[i]

        # 5. Validar si hay varios máximos
        contador = 0
        for i in range(len(conteo_productos)):
            if conteo_productos[i] == mayor:
                contador = contador + 1

        # 6. Mostrar resultados
        if contador == 1:
            print(f"¡{nombre_producto} es el más vendido!")
        else:
            print("")
            print("¡Hay máximos iguales!")
            print("Los más vendidos fueron: ")
            for i in range(len(conteo_productos)):
                if conteo_productos[i] == mayor:
                    print(lista_productos[i])

    def buscarId(self):
        print("")
        print("BUSCAR ID")
        id = int(input("Ingrese ID a buscar: "))
        encontrado = False
        for i in range(len(self.getVentas())):
            if id == self.getVentas()[i][0]:
                encontrado = True
                print(f"¡Encontrado! Nombre cliente: {self.getVentas()[i][1]}")
                break
        if not encontrado:
            print(f"No se encontró el ID {id}...")

# Método principal
def main():
    print("Ejercicio A | Jesús Domínguez")
    a = Ventas()
    #a.setVentas([[1,"Juan","CC",123,"Manzanas",3,2500,7500], [2,"Santiago","TI",345,"Peras",2,2000,4000], [3,"Pedro","OTRO",678,"Uvas",4,3000,12000]])
    a.llenarDatos()
    a.mostrarDatos()
    a.totalVentas()
    a.productoMasVendido()
    a.buscarId()

# Llamar método principal
main()