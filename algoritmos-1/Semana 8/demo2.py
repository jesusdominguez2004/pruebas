# Semana 8 | Algoritmos I

# Creador de vectores
class Vectores():
    # Constructor
    def __init__(self):
        self.vector1 = []
    
    # Set() and get()
    def setVector1(self, v1:list):
        self.vector1 = v1

    def getVector1(self):
        return self.vector1
    
    # Llenar vector
    def llenarVector(self, tam:int):
        for i in range(tam):
            elemento = int(input("Ingrese un elemento: "))
            self.vector1.append(elemento)

    # Mostrar vector
    def mostrarVector(self):
        print("")
        print("MOSTRAR VECTOR")
        for i in self.vector1:
            print(i)

    # Mostar vector invertido
    def mostrarVectorInvertido(self):
        print("")
        print("MOSTRAR VECTOR INVERTIDO")
        i = 0
        while i < len(self.vector1):
            print(self.vector1[len(self.vector1) - 1 - i])
            i = i + 1

    # Promedio de los elementos del vector
    def promedioElementosVector(self):
        print("")
        print("PROMEDIO ELEMENTOS")

        longitud = len(self.getVector1())
        acumulador = 0
        for i in self.getVector1():
            acumulador = acumulador + i
        
        promedio = round(acumulador / longitud, 2)
        print(promedio)

    # Mayor y menor
    def mayorMenorVector(self):
        print("")
        print("ELEMENTO MAYOR Y MENOR")
        
        mayor = self.getVector1()[0]
        menor = self.getVector1()[0]

        i = 0
        while i < len(self.getVector1()):

            if self.getVector1()[i] > mayor:
                mayor = self.getVector1()[i]

            if self.getVector1()[i] < menor:
                menor = self.getVector1()[i]

            i = i + 1

        print(f"Mayor: {mayor}")
        print(f"Menor: {menor}")

    # Cantidad positivos y negativos
    def positivosNegativosVector(self):
        print("")
        print("CANTIDAD POSITIVOS Y NEGATIVOS")

        positivos = 0
        negativos = 0

        i = 0
        while i < len(self.getVector1()):

            if self.getVector1()[i] > 0:
                positivos = positivos + 1

            if self.getVector1()[i] < 0:
                negativos = negativos + 1

            i = i + 1

        print(f"Positivos: {positivos}")
        print(f"Negativos: {negativos}")

# Operador de vectoress
class OperadorVectores():
    pass

# Método principal
def main():
    # Objeto 1
    tam = int(input("Ingrese el tamaño del vector: "))
    a = Vectores()
    a.llenarVector(tam)
    a.mostrarVector()
    a.mostrarVectorInvertido()
    a.promedioElementosVector()
    a.mayorMenorVector()
    a.positivosNegativosVector()

    # Objeto 2
    tam = int(input("Ingrese el tamaño del vector: "))
    b = Vectores()
    b.llenarVector(tam)
    b.mostrarVector()
    a.mostrarVectorInvertido()
    a.promedioElementosVector()
    a.mayorMenorVector()
    a.positivosNegativosVector()

    # Objeto 3
    tam = int(input("Ingrese el tamaño del vector: "))
    c = Vectores()
    c.llenarVector(tam)
    c.mostrarVector()
    a.mostrarVectorInvertido()
    a.promedioElementosVector()
    a.mayorMenorVector()
    a.positivosNegativosVector()

# Llamar método principal
main()