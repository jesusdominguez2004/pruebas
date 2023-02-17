class Ventas:
    def __init__(self):
        self.codigo = []
        self.users = []
        self.productos = []
        self.total= []

    def setCodigo(self, x:list):
        self.codigo = x

    def getCodigo(self):
        return self.codigo

    def setUser(self, x:list):
        self.users = x

    def getUser(self):
        return self.users

    def setProductos(self, x:list):
        self.productos = x

    def getProductos(self):
        return self.productos

    def setTotales(self, x:list):
        self.total = x

    def getTotales(self):
        return self.total

    def guardarVenta(self):
        n = int(input("ingrese el numero de registro en venta: "))
        i = 0
        while i < n:
            codigo = int(input(f"ingrese el código venta {i + 1}: "))
            usuario = input(f"ingrese el usuario venta {i + 1}: ")
            producto = input(f"ingrese el producto venta {i + 1}: ")
            self.getCodigo().append(codigo)
            self.getUser().append(usuario)
            self.getProductos().append(producto)
            if producto == "computador" or producto == "Computador" or producto == "COMPUTADOR": 
                total = 500000
            if producto == "tablet" or producto == "Tablet" or producto == "TABLET": 
                total = 200000
            if producto == "celular" or producto == "Celular" or producto == "CELULAR": 
                total = 100000
            self.getTotales().append(total)
            i = i + 1

    def mostarVenta(self):
        print("")
        print("mostrar la venta...")
        print("codigos venta", self.getCodigo())
        print("usuarios venta", self.getUser())
        print("producto venta", self.getProductos())
        print("totales venta", self.getTotales())

    def metodo1(self):
        print("")
        print("dado un codigo de venta retorne el producto comprado...")
        codigo = input("ingrese el código a buscar: ")
        codigo = int(codigo)
        encontrado = False
        i = 0
        while i < len(self.getCodigo()):
            if codigo == self.getCodigo()[i]:
                file = open("metodo1.txt", "w")
                print(self.getProductos()[i])
                file.write(self.getProductos()[i])
                file.close()
                encontrado = True
                break
            i = i + 1
        if encontrado == False:
            print(codigo, "no está en Ventas.self.getCodigo()")

    def metodo2(self):
        print("")
        print("dato un usuario retorne todas las compras que este realizo...")
        usuario = input("ingrese el usuario a buscar: ")
        encontrado = False 
        file = open("metodo2.txt", "w")
        i = 0
        while i < len(self.getUser()):
            if usuario == self.getUser()[i]:
                print(self.getProductos()[i] + " " + "$" + str(self.getTotales()[i]))
                file.write(self.getProductos()[i] + " " + "$" + str(self.getTotales()[i]) + "\n")
                encontrado = True
            i = i + 1
        file.close()
        if encontrado == False:
            print(usuario, "no está en Ventas.self.getUser()")

    def metodo3(self):
        print("")
        print("indique el promedio total de ventas...")
        sumatoria = 0
        i = 0
        while i < len(self.getTotales()):
            sumatoria = sumatoria + self.getTotales()[i]
            i = i + 1
        promedio = round(sumatoria / len(self.getTotales()), 3)
        file = open("metodo3.txt", "w")
        print("promedio ventas $" + str(promedio))
        file.write("promedio ventas $" + str(promedio))
        file.close()            

    def metodo4(self):
        print("")
        print("indique el producto mas vendido...")

        computadores = 0
        tablets = 0
        celulares = 0
        i = 0
        while i < len(self.getProductos()):
            if self.getProductos()[i] == "computador" or self.getProductos()[i] == "Computador" or self.getProductos()[i] == "COMPUTADOR": 
                computadores = computadores + 1
            if self.getProductos()[i] == "tablet" or self.getProductos()[i] == "Tablet" or self.getProductos()[i] == "TABLET": 
                tablets = tablets + 1
            if self.getProductos()[i] == "celular" or self.getProductos()[i] == "Celular" or self.getProductos()[i] == "CELULAR": 
                celulares = celulares + 1 
            i = i + 1
        cantidades = []
        cantidades.append(computadores)
        cantidades.append(tablets)
        cantidades.append(celulares)
        print("computadores se compro " + str(cantidades[0]) + " veces")
        print("tablets se compro " + str(cantidades[1]) + " veces")
        print("celulares se compro " + str(cantidades[2]) + " veces")
        if cantidades[0] > cantidades[1] and cantidades[0] > cantidades[2]:
            print("computador fue el mas vendido")
            file = open("metodo4.txt", "w")
            file.write("computador fue el mas vendido")
            file.close()
        elif cantidades[1] > cantidades[0] and cantidades[1] > cantidades[2]:
            print("tablet fue el mas vendido")
            file = open("metodo4.txt", "w")
            file.write("tablet fue el mas vendido")
            file.close()
        elif cantidades[2] > cantidades[0] and cantidades[2] > cantidades[1]:
            print("celular fue el mas vendido")
            file = open("metodo4.txt", "w")
            file.write("celular fue el mas vendido")
            file.close()
        elif cantidades[0] == cantidades[1] and cantidades[0] == cantidades[2]:
            print("todos los productos se vendieron igual")
            file = open("metodo4.txt", "w")
            file.write("todos los productos se vendieron igual")
            file.close()
        elif cantidades[0] == cantidades[1] and cantidades[0] != cantidades[2]:
            print("computadores y tablets se vendieron igual")
            file = open("metodo4.txt", "w")
            file.write("computadores y tablets se vendieron igual")
            file.close()
        elif cantidades[0] != cantidades[1] and cantidades[0] == cantidades[2]:
            print("computadores y celulares se vendieron igual")
            file = open("metodo4.txt", "w")
            file.write("computadores y celulares se vendieron igual")
            file.close()
        elif cantidades[1] == cantidades[2] and cantidades[1] != cantidades[0]:
            print("tablets y celulares se vendieron igual")
            file = open("metodo4.txt", "w")
            file.write("tablets y celulares se vendieron igual")
            file.close()
        else:
            print("Error")
            file = open("metodo4.txt", "w")
            file.write("Error en producto mas vendido")
            file.close()

    def metodo5(self):
        print("")
        print("dado un producto retorne todos los usuarios que lo compraron...")
        producto = input("ingrese el producto a buscar: ")
        encontrado = False 
        file = open("metodo5.txt", "w")
        i = 0
        while i < len(self.getProductos()):
            if producto == self.getProductos()[i]:
                print(self.getUser()[i])
                file.write(self.getUser()[i] + "\n")
                encontrado = True
            i = i + 1
        file.close()
        if encontrado == False:
            print(producto, "no está en Ventas.self.getProductos()")

def main():
    a = Ventas()
    a.guardarVenta()
    a.mostarVenta()
    a.metodo1()
    a.metodo2()
    a.metodo3()
    a.metodo4()  
    a.metodo5()
main()