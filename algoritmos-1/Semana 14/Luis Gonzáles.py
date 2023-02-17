import json

class Laptops:
    def __init__(self) -> None:
        self.__nombre = None
        self.__referencia = None
        self.__precio = None
        self.__marca = None 
        self.__color = None
        self.__json = None
        self.__diccionario = None
        self.__archivo = None
    
    def __str__(self) -> str:
        return f"NOMBRE: {self.__nombre}\nREFERENCIA: {self.__referencia}\nPRECIO: {self.__precio}\nMARCA: {self.__marca}\nCOLOR: {self.__color}\nJSON: {self.__json}\nDICCIONARIO: {self.__diccionario}\nARCHIVO: {self.__archivo}"

    def set_nombre(self, nombre:str):
        self.__nombre = nombre

    def get_nombre(self) -> str:
        return self.__nombre

    def set_referencia(self, referencia:str):
        self.__referencia = referencia

    def get_referencia(self) -> str:
        return self.__referencia

    def set_precio(self, precio:float) -> float:
        self.__precio = precio

    def get_precio(self) -> float:
        return self.__precio

    def set_marca(self, marca:str):
        self.__marca = marca

    def get_marca(self) -> str:
        return self.__marca

    def set_color(self, color:str):
        self.__color = color

    def get_color(self) -> str:
        return self.__color

    def set_json(self, json:str):
        self.__json = json

    def get_json(self) -> str:
        return self.__json

    def set_diccionario(self, diccionario:dict):
        self.__diccionario = diccionario

    def get_diccionario(self) -> dict:
        return self.__diccionario

    def set_archivo(self, archivo:str):
        self.__archivo = archivo

    def get_archivo(self) -> str:
        return self.__archivo

    def menu(self):
        self.set_diccionario({})

        print("1. Registrar\n2. Consultar\n3. Editar")
        menu = input("¿Qué desea hacer?: ")

        if menu == "1":
            while True:
                nombre_archivo = input("Ingrese nombre archivo: ")
                nombre = input("Ingrese nombre laptop: ")
                referencia = input("Ingrese la referencia: ")
                precio = float(input("Ingrese el precio: $ "))
                marca = input("Ingrese la marca: ")
                color = input("Ingrese el color: ")

                self.set_archivo(nombre_archivo)
                self.set_nombre(nombre)
                self.set_referencia(referencia)
                self.set_precio(precio)
                self.set_marca(marca)
                self.set_color(color)
                self.get_diccionario()[nombre] = {
                    "Referencia": referencia,
                    "Precio": precio,
                    "Marca": marca,
                    "Color": color
                }

                with open(nombre_archivo + ".txt" , "w") as archivo:
                    json.dump(self.get_diccionario(), archivo)
                    x = json.dumps(self.get_diccionario())
                    self.set_json(x)

                opc = input("¿Desea agregar otra laptop? S/N: ").upper()
                if opc == "N":
                    break

        if menu == "2":
            nombre_archivo = input("Ingrese nombre archivo: ")
            with open(nombre_archivo + ".txt", "r") as archivo:
                # Obtener json
                self.set_diccionario(archivo.read())
                print("JSON:", type(self.get_diccionario()), self.get_diccionario())

                # Convertir a diccionario
                self.set_diccionario(json.loads(self.get_diccionario()))
                print("DICCIONARIO:", type(self.get_diccionario()), self.get_diccionario())

                for i in self.get_diccionario():
                    print(f"NOMBRE LAPTOP: {i} | REFERENCIA: {self.get_diccionario()[i]['Referencia']} | PRECIO: {self.get_diccionario()[i]['Precio']} | MARCA: {self.get_diccionario()[i]['Marca']} | COLOR: {self.get_diccionario()[i]['Color']}")
                    
        if menu == "3":
            nombre_archivo = input("Ingrese nombre archivo: ")
            with open(nombre_archivo + ".txt", "r") as archivo:
                # 1. Obtener json de txt
                self.set_diccionario(archivo.read())

                # 2. Convertir a diccionario Python
                self.set_diccionario(json.loads(self.get_diccionario()))

                # 3. Modificarlo 
                print("Laptos almacenadas:")
                for i in self.get_diccionario():
                    print(f"- {i}")

                laptop = input("¿Qué laptop desea modificar?: ")
                if laptop in self.get_diccionario():
                    print(f"Referencia {laptop}: {self.get_diccionario()[laptop]['Referencia']}")
                    print(f"Precio {laptop}: {self.get_diccionario()[laptop]['Precio']}")
                    print(f"Marca {laptop}: {self.get_diccionario()[laptop]['Marca']}")
                    print(f"Color {laptop}: {self.get_diccionario()[laptop]['Color']}")
                    atributo = input("¿Qué desea cambiar?: ").capitalize()

                    if atributo in  self.get_diccionario()[laptop]:
                        if type(self.get_diccionario()[laptop][atributo]) == float:
                            valor_nuevo = input(f"Ingrese valor nuevo '{atributo}' de laptop '{laptop}': $")
                            self.get_diccionario()[laptop][atributo] = float(valor_nuevo)
                        else:
                            valor_nuevo = input(f"Ingrese valor nuevo '{atributo}' de laptop '{laptop}': ")
                            self.get_diccionario()[laptop][atributo] = valor_nuevo
                    else:
                        print(f"{atributo} no es un atributo válido")
                else:
                    print(f"{laptop} no está almacenada...")

                with open(nombre_archivo + ".txt", "w") as archivo:
                    # 4. Reemplazar json nuevo a txt 
                    json.dump(self.get_diccionario(), archivo)

def main():
    ejemplo_1 = Laptops()
    ejemplo_1.menu()

main()