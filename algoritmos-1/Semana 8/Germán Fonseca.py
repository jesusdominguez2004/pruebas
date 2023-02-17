# n números | Con listas

"""
- Mayor
- Pares
- Impares
- Suma pares e impares
- Promedio pares e impares
"""

# Clase creadora de números
class Numeros():
    def __init__(self):
        self.numeros = []

    def setNumeros(self, x:list):
        self.numeros = x
    
    def getNumeros(self):
        return self.numeros

    def llenarNumeros(self):
        cantidad = input("Ingrese la cantidad de números: ")

        while cantidad.isnumeric() == False or int(cantidad) <= 0:
            print("Datos no válidos...")
            print("Cantidad debe ser mayor que cero")

        cantidad = int(cantidad) 

        for i in range(cantidad):
            x = int(input(f"Ingrese un número [{i+1}]: "))
            while x == 0:
                print("Datos no válidos...")
                print("No se permiten ceros")
                x = int(input(f"Ingrese un número [{i+1}]: "))
            self.getNumeros().append(x)

    # Número mayor
    def mayor(self):
        print("")
        mayor = self.getNumeros()[0]

        for i in range(len(self.getNumeros())):
            if self.getNumeros()[i] > mayor:
                mayor = self.getNumeros()[i]

        print(f"NÚMERO MAYOR: {mayor}")

    # Todo pares
    def todoPares(self):
        print("")
        # Cantidad pares
        cantidad_pares = 0
        for i in range(len(self.getNumeros())):
            if self.getNumeros()[i] > 0:
                cantidad_pares = cantidad_pares + 1
        print(f"CANTIDAD PARES: {cantidad_pares}")

        # Suma pares
        suma_pares = 0
        for i in range(len(self.getNumeros())):
            if self.getNumeros()[i] > 0:
                suma_pares = suma_pares + self.getNumeros()[i]
        print(f"SUMA PARES: {suma_pares}")

        # Promedio pares
        if cantidad_pares == 0:
            print("PROMEDIO PARES: 0")
        else:
            promedio_pares = suma_pares / cantidad_pares
            print(f"PROMEDIO PARES: {promedio_pares}")
        
    # Todo impares
    def todoImpares(self):
        print("")
        # Cantidad impares
        cantidad_impares = 0
        for i in range(len(self.getNumeros())):
            if self.getNumeros()[i] < 0:
                cantidad_impares = cantidad_impares + 1
        print(f"CANTIDAD IMPARES: {cantidad_impares}")

        # Suma impares
        suma_impares = 0
        for i in range(len(self.getNumeros())):
            if self.getNumeros()[i] < 0:
                suma_impares = suma_impares + self.getNumeros()[i]
        print(f"SUMA IMPARES: {suma_impares}")

        # Promedio impares
        if cantidad_impares == 0:
            print("PROMEDIO IMPARES: 0")
        else:
            promedio_impares = suma_impares / cantidad_impares
            print(f"PROMEDIO IMPARES: {promedio_impares}")

# Método principal
def main():
    a = Numeros()
    a.llenarNumeros()
    # print(a.getNumeros())
    a.todoPares()
    a.todoImpares()

# Llamar método principal
main()