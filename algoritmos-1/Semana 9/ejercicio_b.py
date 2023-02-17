# Ejercicio B

# ID | NOMBRE | INGREDIENTE 1, 2, 3 | VALOR | CANTIDAD | TOTAL

# 1) Total ventas
# 2) Producto más vendido
# 3) Búsqueda por ID

class MenuRestaurante():
    def __init__(self):
        self.registros = []

    def setRegistros(self, x:list):
        self.registros = x

    def getRegistros(self):
        return self.registros

    def llenarDatos(self, filas:int):
        print("LLENAR DATOS")
        for i in range(filas):
            self.getRegistros().append([])
            for j in range(8):
                if j == 0:
                    id = int(input("Ingrese ID comida: "))
                    self.getRegistros()[i].append(id)
                if j == 1:
                    nombre = input("Ingrese NOMBRE comida: ")
                    self.getRegistros()[i].append(nombre)
                if j == 2:
                    ing_1 = input("Ingrese INGREDIENTE 1 comida: ")
                    self.getRegistros()[i].append(ing_1)
                if j == 3:
                    ing_2 = input("Ingrese INGREDIENTE 2 comida: ")
                    self.getRegistros()[i].append(ing_2)
                if j == 4:
                    ing_2 = input("Ingrese INGREDIENTE 3 comida: ")
                    self.getRegistros()[i].append(ing_2)
                if j == 5:
                    valor = int(input("Ingrese VALOR comida: "))
                    self.getRegistros()[i].append(valor)
                if j == 6:
                    cantidad = int(input("Ingrese CANTIDAD comida: "))
                    self.getRegistros()[i].append(cantidad)
                if j == 7:
                    total = valor * cantidad
                    self.getRegistros()[i].append(total)
            print("")
    
    def mostrarDatos(self):
        print("MOSTRAR DATOS")
        # print(self.getRegistros())
        for i in range(len(self.getRegistros())):
            print(f"{i+1}. ID: {self.getRegistros()[i][0]} | NOMBRE: {self.getRegistros()[i][1]} | INGREDIENTE 1: {self.getRegistros()[i][2]} | INGREDIENTE 2: {self.getRegistros()[i][3]} | INGREDIENTE 3: {self.getRegistros()[i][4]} | VALOR: ${self.getRegistros()[i][5]} | CANTIDAD: {self.getRegistros()[i][6]} | TOTAL: ${self.getRegistros()[i][7]}")

    def totalVentas(self):
        print("")
        print("TOTAL VENTAS")
        total_ventas = 0
        for i in range(len(self.getRegistros())):
            total_ventas = total_ventas + self.getRegistros()[i][7]
        print(f"${total_ventas}")

    def productoMasVendido(self):
        print("")
        print("PRODUCTO MÁS VENDIDO")
        # 1. Lista de productos sin repetir
        lista_productos = []
        for i in range(len(self.getRegistros())):
            if self.getRegistros()[i][1] not in lista_productos:
                lista_productos.append(self.getRegistros()[i][1])

        # 2. Lista de contadores productos
        conteo_productos = []
        contador = 0
        for i in range(len(lista_productos)):
            for j in range(len(self.getRegistros())):
                if lista_productos[i] == self.getRegistros()[j][1]:
                    contador = contador + self.getRegistros()[j][6] # Cantidad
            conteo_productos.append(contador)
            contador = 0
        
        # 3. Mostrar productos y sus cantidades
        print("Encontrados:")
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
        for i in range(len(self.getRegistros())):
            if id == self.getRegistros()[i][0]:
                encontrado = True
                print(f"¡Encontrado! Nombre producto: {self.getRegistros()[i][1]}")
                break
        if not encontrado:
            print(f"No se encontró el ID {id}...")

# Método principal
def main():
    registro_1 = MenuRestaurante()
    registro_1.llenarDatos(2) # llenarDatos(FILAS)
    registro_1.mostrarDatos()
    registro_1.totalVentas()
    registro_1.productoMasVendido()
    registro_1.buscarId()

# Llamar método principal
main()