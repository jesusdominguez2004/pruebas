# INDICADOR 3: Sistema de Ventas

class SistemaVentas:
    # Constructor
    def __init__(self) -> None:
        self.__codigos = []
        self.__usuarios = []
        self.__productos = []
        self.__totales= []

    # Setter and getters
    def set_codigos(self, codigos:list) -> None:
        self.__codigos = codigos

    def get_codigos(self) -> list:
        return self.__codigos

    def set_usuarios(self, usuarios:list) -> None:
        self.__usuarios = usuarios

    def get_usuarios(self) -> list:
        return self.__usuarios

    def set_productos(self, productos:list) -> None:
        self.__productos = productos

    def get_productos(self) -> list:
        return self.__productos

    def set_totales(self, totales:list) -> None:
        self.__totales = totales

    def get_totales(self) -> list:
        return self.__totales

    # Llenar los ventores y mostrar sus datos
    def llenar_datos(self) -> None:
        ventas = int(input("Ingrese número de ventas: "))
        for i in range(ventas):
            codigo = int(input(f"Ingrese código venta {i + 1}: "))
            usuario = input(f"Ingrese usuario venta {i + 1}: ").capitalize()
            producto = input(f"Ingrese producto venta {i + 1} (computador, tablet o celular): ").capitalize()
            
            if producto == "Computador": total = 500_000
            elif producto == "Tablet": total = 200_000
            elif producto == "Celular": total = 100_000
            else: total = 0

            self.get_codigos().append(codigo)
            self.get_usuarios().append(usuario)
            self.get_productos().append(producto)
            self.get_totales().append(total)
            print("")

    def mostrar_datos(self) -> str:
        print("MOSTRAR DATOS")
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        print("| CÓDIGOS | USUARIOS |  PRODUCTOS  |  TOTALES |")
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        for i in range(len(self.get_codigos())):
            codigo = self.get_codigos()[i]
            usuario = self.get_usuarios()[i]
            producto = self.get_productos()[i]
            total = self.get_totales()[i]
            print(f"|{codigo:^9}|{usuario:^10}|{producto:^13}|${total:^9}|")
            print("- - - - - - - - - - - - - - - - - - - - - - - -")

    # Métodos de almacenamiento en txt
    def codigo_producto(self) -> str:
        print("\nMÉTODO 1")
        codigo_buscar = int(input("Ingrese código a buscar: "))
        if codigo_buscar not in self.get_codigos():
            print(f"{codigo_buscar} no está en el sistema ventas...")
        else:
            for i in range(len(self.get_codigos())):
                if self.get_codigos()[i] == codigo_buscar:
                    print(f"Su producto es {self.get_productos()[i]}")
                    with open("3 - Método 1.txt", "w", encoding="utf-8") as archivo:
                        archivo.write(f"{self.get_productos()[i]}")
                    break

    def compras_usuarios(self) -> str:
        print("\nMÉTODO 2")
        usuario_buscar = input("Ingrese usuario a buscar: ").capitalize()
        if usuario_buscar not in self.get_usuarios():
            print(f"{usuario_buscar} no está en el sistema ventas...")
        else:
            with open("3 - Método 2.txt", "w", encoding="utf-8") as archivo:
                contador = 1
                for i in range(len(self.get_usuarios())):
                    if self.get_usuarios()[i] == usuario_buscar:
                        print(f"Compra {contador} de {usuario_buscar}: {self.get_productos()[i]} ${self.get_totales()[i]}")
                        archivo.write(f"Compra {contador} de {usuario_buscar}: {self.get_productos()[i]} ${self.get_totales()[i]}\n")
                        contador = contador + 1

    def promedio_ventas(self) -> str:
        print("\nMÉTODO 3")
        sumatoria = 0
        for i in range(len(self.get_totales())):
            sumatoria = sumatoria + self.get_totales()[i]

        promedio = sumatoria / len(self.get_totales())
        promedio = round(promedio, 2)
        print(f"El promedio de ventas es: ${promedio}")
        with open("3 - Método 3.txt", "w", encoding="utf-8") as archivo:
            archivo.write(f"El promedio de ventas es: ${promedio}")

    def producto_mas_vendido(self) -> str:
        print("\nMÉTODO 4")
        # 1. Lista de productos sin repetir
        productos = ["Computador", "Tablet", "Celular"]

        # 2. Lista de contadores productos
        cantidades = []
        contador = 0
        for i in productos:
            for j in self.get_productos():
                if i == j:
                    contador = contador + 1
            cantidades.append(contador)
            contador = 0

        # 3. Mostrar productos y sus cantidades
        for i in range(len(productos)):
            print(f"{productos[i]} fue comprado {cantidades[i]} veces")

        # 4. Contador mayor
        mayor = cantidades[0]
        nombre = productos[0]
        for i in range(len(cantidades)):
            if cantidades[i] > mayor:
                mayor = cantidades[i]
                nombre = productos[i]

        # 5. Validar si hay varios máximos
        contador = 0
        for i in cantidades: 
            if i == mayor: 
                contador = contador + 1

        # 6. Mostrar resultados
        if contador == 1:
            print(f"¡{nombre} es el que más se venció! ({mayor} compras)")
            with open("3 - Método 4.txt", "w", encoding="utf-8") as archivo:
                archivo.write(f"¡{nombre} es el que más se venció! ({mayor} compras)")
        else:
            with open("3 - Método 4.txt", "w") as archivo:
                print("Los más vendidos fueron:")
                for i in range(len(cantidades)):
                    if cantidades[i] == mayor:
                        print(f"{productos[i]} ({mayor} compras)")
                        archivo.write(f"{productos[i]} ({mayor} compras)\n")

    def usarios_productos(self) -> str:
        print("\nMÉTODO 5")
        producto_buscar = input("Ingrese producto a buscar: ").capitalize()
        if producto_buscar not in self.get_productos():
            print(f"{producto_buscar} no está en el sistema ventas...")
        else:
            with open("3 - Método 5.txt", "w", encoding="utf-8") as archivo:
                contador = 1
                for i in range(len(self.get_productos())):
                    if self.get_productos()[i] == producto_buscar:
                        print(f"Usuario {contador} con {producto_buscar}: {self.get_usuarios()[i]}")  
                        archivo.write(f"Usuario {contador} con {producto_buscar}: {self.get_usuarios()[i]}\n")
                        contador = contador + 1

def main():
    venta_1 = SistemaVentas()
    venta_1.llenar_datos()
    venta_1.mostrar_datos()

    venta_1.codigo_producto()
    venta_1.compras_usuarios()
    venta_1.promedio_ventas()
    venta_1.producto_mas_vendido()
    venta_1.usarios_productos()

main()