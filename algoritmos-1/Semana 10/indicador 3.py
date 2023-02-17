# Indicador 3 | Jesús Domínguez

class Ventas():
    def __init__(self):
        self.__ventas = []

    def setVentas(self, x:list):
        self.__ventas = x

    def getVentas(self):
        return self.__ventas

    def llenarDatos(self):
        print("LLENAR DATOS")
        filas = int(input("Ingrese la cantidad de filas: "))
        for i in range(filas):
            self.getVentas().append([])
            for j in range(8):
                if j == 0:
                    id = int(input(f"Ingrese ID cliente {i + 1}: "))
                    self.getVentas()[i].append(id)

                if j == 1:
                    producto = input(f"Ingrese PRODUCTO cliente {i + 1}: ")
                    self.getVentas()[i].append(producto)

                if j == 2:
                    cantidad = int(input(f"Ingrese CANTIDAD cliente {i + 1}: "))
                    self.getVentas()[i].append(cantidad)

                if j == 3:
                    valor_unitario = eval(input(f"Ingrese VALOR UNITARIO cliente {i + 1}: "))
                    self.getVentas()[i].append(valor_unitario)

                if j == 4:
                    total = valor_unitario * cantidad
                    self.getVentas()[i].append(total)

                if j == 5:
                    dia = int(input(f"Ingrese DÍA cliente {i + 1}: "))
                    self.getVentas()[i].append(dia)

                if j == 6:
                    mes = int(input(f"Ingrese MES cliente {i + 1}: "))
                    self.getVentas()[i].append(mes)

                if j == 7:
                    año = int(input(f"Ingrese AÑO cliente {i + 1}: "))
                    self.getVentas()[i].append(año)

            print("")

    def mostrarDatos(self):
        print("MOSTRAR DATOS")
        # print(self.getVentas())
        for i in range(len(self.getVentas())):
            print(f"{i+1}. ID: {self.getVentas()[i][0]} | PRODUCTO: {self.getVentas()[i][1]} | CANTIDAD: {self.getVentas()[i][2]} | VALOR UNITARIO: ${self.getVentas()[i][3]} | TOTAL: ${self.getVentas()[i][4]} | DÍA: {self.getVentas()[i][5]} | MES: {self.getVentas()[i][6]} | AÑO: {self.getVentas()[i][7]}")
        print("")

    def productoMasVendidoMes(self):
        print("PRODUCTO MÁS VENDIDO MES")
        mes_buscar = int(input("Ingrese mes a buscar: "))

        encontrado = False
        for i in range(len(self.getVentas())):
            if mes_buscar == self.getVentas()[i][6]:
                encontrado = True

        if not encontrado:
            print("Mes no encontrado, producto más vendido: N/A")
        else:
            # La Moda es un procedimiento muy complejo
            # Así que enumero los pasos:

            # 1. Lista de productos sin repetir + SOLO MES INGRESADO
            lista_productos = []
            for i in range(len(self.getVentas())):
                if mes_buscar == self.getVentas()[i][6]:
                    if self.getVentas()[i][1] not in lista_productos:
                        lista_productos.append(self.getVentas()[i][1])

             # 2. Lista de contadores productos + SOLO MES INGRESADO
            conteo_productos = []
            contador = 0
            for i in range(len(lista_productos)):
                for j in range(len(self.getVentas())):
                    if mes_buscar == self.getVentas()[i][6]:
                        if lista_productos[i] == self.getVentas()[j][1]:
                            contador = contador + self.getVentas()[j][2] # Cantidad
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
        print("")
       
    def totalVentasProducto(self):
        print("TOTAL VENTAS PRODUCTO")
        producto_buscar = input("Ingrese producto a buscar: ")

        encontrado = False
        total = 0
        for i in range(len(self.getVentas())):
            if producto_buscar == self.getVentas()[i][1]:
                total = total + self.getVentas()[i][4]
                encontrado = True
        if not encontrado:
            print("Producto no encontrado, total: $0")
        else:
            print(f"${total}")
        print("")

    def totalVentasAño(self):
        print("TOTAL VENTAS AÑO")
        año_buscar = int(input("Ingrese año a buscar: "))

        encontrado = False
        total = 0
        for i in range(len(self.getVentas())):
            if año_buscar == self.getVentas()[i][7]:
                total = total + self.getVentas()[i][4]
                encontrado = True
        if not encontrado:
            print("Año no encontrado, total: $0")
        else:
            print(f"${total}")
        print("")

    def ventasMenoresA(self):
        print("VENTAS MENORES A")
        valor_referencia = eval(input("Ingrese valor referencia: $"))
        
        encontrados = False
        for i in range(len(self.getVentas())):
            if self.getVentas()[i][4] < valor_referencia:
                print(f"${self.getVentas()[i][4]}")
                encontrados = True

        if not encontrados:
            print("Ninguna venta registrada es menor que valor referencia...")
        print("")

    def promedioVentas(self):
        print("PROMEDIO VENTAS")
        suma_ventas = 0
        for i in range(len(self.getVentas())):
            suma_ventas = suma_ventas + self.getVentas()[i][4]

        # Evitar división por cero
        if suma_ventas == 0:
            print("Sumatoria ventas: $0")
            print("Promedio ventas: $0")
        else:
            promedio_ventas = round(suma_ventas / len(self.getVentas()), 2)
            print(f"Sumatoria ventas: ${suma_ventas}")
            print(f"Promedio ventas: ${promedio_ventas}")

def main():
    matriz1 = Ventas()
    #matriz1.setVentas([[1, "arroz", 1, 7000, 7000, 1, 4, 22], [2, "tomate", 2, 4000, 8000, 2, 4, 22], [3, "arroz", 3, 7000, 14000, 1, 4, 22], [4, "tomate", 3, 4000, 12000, 2, 4, 22]])
    matriz1.llenarDatos()
    matriz1.mostrarDatos()

    matriz1.productoMasVendidoMes()
    matriz1.totalVentasProducto()
    matriz1.totalVentasAño()
    matriz1.ventasMenoresA()
    matriz1.promedioVentas()

main()