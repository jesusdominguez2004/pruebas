# Actividad 1 | Sistema de ventas | Jesús Domínguez

"""
Id | Nombre | Tipo doc | Núm doc | Producto | Cantidad | Valor | Total

Métodos: 
    1. Total de ventas
    2. Producto más vendido
    3. Búsqueda por Id o Cédula
"""

# Clase ventas
class Ventas():
    # Constructor
    def __init__(self):
        self.matriz = []

    # Set()
    def setMatriz(self, matriz:list):
        self.matriz = matriz

    # Get()
    def getMatriz(self):
        return self.matriz

    # Métodos
    def llenarDatos(self):
        print("LLENAR DATOS")
        lista_productos = ["Arroz", "Pastas", "Manzana", "Lentejas", "Uvas"]
        lista_precios = [2500, 1600, 3000, 2300, 4000]
        lista_tipDoc = ["Cédula", "Tarjeta de identidad", "Otro"]
        listas_numDoc = []

        cantidad_registros = int(input("Ingrese la cantidad de registros: "))
        # Filas 
        for i in range(cantidad_registros):
            self.getMatriz().append([])

            # Nombre
            nombre = input(f"Ingrese el nombre (cliente {i+1}): ")

            # Tipo documento
            x = 0
            while x < len(lista_tipDoc):
                print(f"{x + 1} = {lista_tipDoc[x]}")
                x = x + 1
            tipoDoc = int(input(f"Ingrese tipo documento (cliente {i+1}): "))
            
            while tipoDoc > len(lista_tipDoc) or tipoDoc < 1:
                print("Datos no validos...")
                tipoDoc = int(input(f"Ingrese tipo documento (cliente {i+1}): "))

            # Número de documento
            numDoc = int(input(f"Ingrese número de documento (cliente {i+1}): "))
            while numDoc in listas_numDoc:
                print("Número de documento repetido...")
                numDoc = int(input(f"Ingrese número de documento (cliente {i+1}): "))
            listas_numDoc.append(numDoc)

            # Producto
            x = 0
            while x < len(lista_productos):
                print(f"{x + 1} = {lista_productos[x]}")
                x = x + 1
            producto = int(input(f"Ingrese el producto (cliente {i+1}): "))

            while producto > len(lista_productos) or producto < 1:
                print("Datos no validos...")
                producto = int(input(f"Ingrese el producto (cliente {i+1}): "))    
            
            # Cantidad
            cantidad = int(input(f"Ingrese la cantidad (cliente {i+1}): "))
            while cantidad < 1:
                print("Datos no validos...")
                cantidad = int(input(f"Ingrese la cantidad (cliente {i+1}): ")) 

            # Valor
            valor = lista_precios[producto - 1]
            producto = lista_productos[producto - 1]
            total = valor * cantidad

            # Almacenar datos
            self.getMatriz()[i].append(i+1)
            self.getMatriz()[i].append(nombre)
            self.getMatriz()[i].append(tipoDoc)
            self.getMatriz()[i].append(numDoc)
            self.getMatriz()[i].append(producto)
            self.getMatriz()[i].append(cantidad)
            self.getMatriz()[i].append(valor)
            self.getMatriz()[i].append(total)

            print("")
        print("¡Proceso de llenado exitoso!")

    # Mostrar datos
    def mostrarDatos(self):
        print("")
        print("MOSTRAR DATOS")
        # Filas
        for i in range(len(self.getMatriz())):
            print(f"{i+1}. NOMBRE: {self.getMatriz()[i][1]} | TIPO DOC: {self.getMatriz()[i][2]} | NÚM DOC: {self.getMatriz()[i][3]} | PRODUCTO: {self.getMatriz()[i][4]} | CANTIDAD: {self.getMatriz()[i][5]} | VALOR: ${self.getMatriz()[i][6]} | TOTAL: ${self.getMatriz()[i][7]}")
    
    # Total de ventas
    def totalVentas(self):
        print("")
        print("TOTAL VENTAS")
        total_ventas = 0
        for i in range(len(self.getMatriz())):
            total_ventas = total_ventas + self.getMatriz()[i][7]
        print(f"${total_ventas}")

    def productoMasVendido(self):
        print("")
        print("PRODUCTO MÁS VENDIDO")

        lista_productos = ["Arroz", "Pastas", "Manzana", "Lentejas", "Uvas"]
        conteo_productos = []
        contador = 0
        i = 0
        while i < len(lista_productos):
            j = 0
            while j < len(self.getMatriz()):
                if lista_productos[i] == self.getMatriz()[j][4]:
                    contador = contador + self.getMatriz()[j][5]
                j = j + 1
            conteo_productos.append(contador)
            contador = 0
            i = i + 1

        # Imprimir productos y sus cantidades
        i = 0
        while i < len(lista_productos):
            print(f"{i + 1}. {lista_productos[i]} (cantidad {conteo_productos[i]})")
            i = i + 1

        # Identificar el mayor
        mas_vendido = conteo_productos[0]
        nombre_producto = lista_productos[0]

        i = 0
        while i < len(conteo_productos):
            if conteo_productos[i] > mas_vendido:
                mas_vendido = conteo_productos[i]
                nombre_producto = lista_productos[i]
            i = i + 1

        # Validar que no hallan máximos iguales
        contador = 0
        i = 0 
        while i < len(conteo_productos):
            if conteo_productos[i] == mas_vendido:
                contador = contador + 1
            i = i + 1

        if contador == 1:
            print(f"¡{nombre_producto} es el más vendido!")
        else:
            print("¡Hay máximos iguales!")
            print("Los más vendidos fueron: ")
            i = 0
            while i < len(conteo_productos):
                if conteo_productos[i] == mas_vendido:
                    print(f"{lista_productos[i]}")
                i = i + 1
    def buscarNumDoc(self):
        numDoc_buscar = int(input("Ingrese CC a buscar: "))
        encontrado = False
        i = 0
        while i < len(self.getMatriz()):
            # Ir buscando
            if numDoc_buscar == self.getMatriz()[i][3]:
                encontrado = True
            # Cambiar registro
            i = i + 1

        # Validar
        if encontrado == False:
            print("Cliente no encontrado...")
        else:
            print("¡Cliente encontrado!")
            i = 0
            while i < len(self.getMatriz()):
                # Ir buscando
                if numDoc_buscar == self.getMatriz()[i][3]:
                    print(f"Nombre: {self.getMatriz()[i][1]}")
                # Cambiar registro
                i = i + 1

# Método principal
def main():
    # Venta 1
    venta1 = Ventas()
    venta1.llenarDatos()
    venta1.mostrarDatos()
    venta1.totalVentas()
    venta1.productoMasVendido()
    venta1.buscarNumDoc()
    
# Llamar método principal
main()