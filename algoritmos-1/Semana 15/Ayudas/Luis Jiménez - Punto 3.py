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
        n = int(input("INGRESE EL NUMERO DE REGISTROS EN VENTA: "))
        i = 0
        while i < n:
            codigo = int(input(f"INGRESE EL CODIGO DE VENTA {i + 1}: "))
            usuario = input(f"INGRESE EL USUARIO DE VENTA {i + 1}: ")
            producto = input(f"INGRESE EL PRODUCTO DE VENTA {i + 1}: ")
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
        print("MOSTRAR DE LA VENTA...")
        print("CODIGOS DE VENTA", self.getCodigo())
        print("USUARIOS DE VENTA", self.getUser())
        print("PRODUCTO DE VENTA", self.getProductos())
        print("TOTALES DE VETA", self.getTotales())

    def metodo1(self):
        print("")
        print("DADO UN CODIGO DE VENTA RETORNE EL RPODUCTO COMPRADO...")
        codigo = input("INGRESE EL CODIGO A BUSCAR: ")
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
        print("DADO UN USUARIO RETORNE TODAS LAS COMPRAS QUE ESTE REALIZO...")
        usuario = input("iINGRESE EL USUARIO A BUSCAR: ")
        encontrado = False 
        file = open("metodo_2.txt", "w")
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
        print("INDIQUE EL PROMEDIO DE VENTAS...")
        sumatoria = 0
        i = 0
        while i < len(self.getTotales()):
            sumatoria = sumatoria + self.getTotales()[i]
            i = i + 1
        promedio = round(sumatoria / len(self.getTotales()), 3)
        file = open("metodo_3.txt", "w")
        print("PROEDIO DE VENTAS $" + str(promedio))
        file.write("promedio ventas $" + str(promedio))
        file.close()            

    def metodo4(self):
        print("")
        print("INDIQUE EL PRODUCTO MAS VENDIDO...")

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
        print("COMPUTADORES SE COMPRO " + str(cantidades[0]) + " VECES")
        print("TABLETS SE COMPRO " + str(cantidades[1]) + " VECES")
        print("CELULARES SE COMPRO " + str(cantidades[2]) + " VECES")
        if cantidades[0] > cantidades[1] and cantidades[0] > cantidades[2]:
            print("COMPUTADOR FUE EL MAS VENDIDO")
            file = open("metodo_4.txt", "w")
            file.write("COMPUTADOR FUE EL MAS VENDIDO")
            file.close()
        elif cantidades[1] > cantidades[0] and cantidades[1] > cantidades[2]:
            print("TABLET FUE EL MAS VENDIDO")
            file = open("metodo_4.txt", "w")
            file.write("TABLET FUE EL MAS VENDIDO")
            file.close()
        elif cantidades[2] > cantidades[0] and cantidades[2] > cantidades[1]:
            print("CELULAR FUE EL MAS VENDIDO")
            file = open("metodo_4.txt", "w")
            file.write("CELULAR FUE EL MAS VENDIDO")
            file.close()
        elif cantidades[0] == cantidades[1] and cantidades[0] == cantidades[2]:
            print("TODOS LOS PRODUCTOS SE VENDIERON IGUAL")
            file = open("metodo_4.txt", "w")
            file.write("TODOS LOS PRODUCTOS SE VENDIERON IGUAL")
            file.close()
        elif cantidades[0] == cantidades[1] and cantidades[0] != cantidades[2]:
            print("COMPUTADORES Y TABLETS SE VENDIERON IGUAL")
            file = open("metodo_4.txt", "w")
            file.write("COMPUTADORES Y TABLETS SE VENDIERON IGUAL")
            file.close()
        elif cantidades[0] != cantidades[1] and cantidades[0] == cantidades[2]:
            print("COMPUTADORES Y CELULARES SE VENDIERON IGUAL")
            file = open("metodo_4.txt", "w")
            file.write("COMPUTADORES Y CELULARES SE VENDIERON IGUAL")
            file.close()
        elif cantidades[1] == cantidades[2] and cantidades[1] != cantidades[0]:
            print("TABLETS Y CEULARES SE VENDIERON IGUAL")
            file = open("metodo_4.txt", "w")
            file.write("TABLETS Y CEULARES SE VENDIERON IGUAL")
            file.close()
        else:
            print("Error")
            file = open("metodo_4.txt", "w")
            file.write("ERROR EN EL PRODUCTO MAS VENDIDO")
            file.close()

    def metodo5(self):
        print("")
        print("DADO UN PRODUCTO RETORNE TODOS LOS USUARIOS QUE LO COMPRARON...")
        producto = input("INGRESE EL PRODUCTO A BUSCAR: ")
        encontrado = False 
        file = open("metodo_5.txt", "w")
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