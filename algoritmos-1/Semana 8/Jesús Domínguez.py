# Tarea | Semana 8 | Jesús Domínguez

# Clase creadora de vectores
class Vectores():
    # Costructor
    def __init__(self):
        self.vector = []

    # Set()
    def setVector(self, vector:list):
        self.vector = vector

    # Get()
    def getVector(self):
        return self.vector

    # Llenar vector
    def llenarVector(self, tam:int):
        i = 0
        while i < tam:
            x = int(input(f"Ingrese el elemento vector[{i}]: "))
            self.vector.append(x)
            i = i + 1
    
    # Mostrar vector
    def mostrarVector(self):
        print("")
        print("MOSTRAR VECTOR")
        i = 0
        while i < len(self.getVector()):
            print(self.getVector()[i])
            i = i + 1

    # Mostar vector invertido
    def mostrarVectorInvertido(self):
        print("")
        print("MOSTRAR VECTOR INVERTIDO")
        i = 0
        while i < len(self.getVector()):
            print(self.getVector()[len(self.getVector()) - 1 - i])
            i = i + 1

    # Promedio de los elementos del vector
    def promedioElementosVector(self):
        print("")
        print("PROMEDIO ELEMENTOS")
        longitud = len(self.getVector())
        acumulador = 0
        i = 0
        while i < len(self.getVector()):
            acumulador = acumulador + self.getVector()[i]
            i = i + 1
        promedio = round(acumulador / longitud, 2)
        print(promedio)

    # Mayor y menor
    def mayorMenorVector(self):
        print("")
        print("ELEMENTO MAYOR Y MENOR")
        mayor = self.getVector()[0]
        menor = self.getVector()[0]
        i = 0
        while i < len(self.getVector()):
            if self.getVector()[i] > mayor:
                mayor = self.getVector()[i]
            if self.getVector()[i] < menor:
                menor = self.getVector()[i]
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
        while i < len(self.getVector()):
            if self.getVector()[i] > 0:
                positivos = positivos + 1
            if self.getVector()[i] < 0:
                negativos = negativos + 1
            i = i + 1
        print(f"Positivos: {positivos}")
        print(f"Negativos: {negativos}")

# Clase operadora de vectores
class OperadorVectores():
    def __init__(self):
        self.v1 = Vectores()
        self.v2 = Vectores()

    def setV1(self, x:Vectores()):
        self.v1 = x

    def getV1(self):
        return self.v1

    def setV2(self, x:Vectores()):
        self.v2 = x

    def getV2(self):
        return self.v2

    # Suma posiciones iguales
    def sumaPosicionesIguales(self):
        print("")
        print("SUMA POSICIONES IGUALES")
        print(f"v1: {self.getV1()}")
        print(f"v2: {self.getV2()}")
        acumulador = 0
        i = 0
        while i < len(self.getV1()):
            acumulador = acumulador + self.getV1()[i] + self.getV2()[i]
            i = i + 1
        print(acumulador)

    # Suma posiciones inversas
    def sumaPosicionesInversas(self):
        print("")
        print("SUMA POSICIONES INVERSAS")
        print(f"v1: {self.getV1()}")
        print(f"v2: {self.getV2()}")
        acumulador = 0
        i = 0
        while i < len(self.getV1()):
            acumulador = acumulador + self.getV1()[i] + self.getV2()[len(self.getV2()) - 1 - i]
            i = i + 1
        print(acumulador)

    # Promedio mayor
    def promedioMayor(self):
        print("")
        print("PROMEDIO MAYOR")
        acumulador1 = 0
        acumulador2 = 0
        i = 0
        while i < len(self.getV1()):
            acumulador1 = acumulador1 + self.getV1()[i]
            acumulador2 = acumulador2 + self.getV2()[i]
            i = i + 1
        promedio1 = round(acumulador1 / len(self.getV1()), 2)
        promedio2 = round(acumulador2 / len(self.getV2()), 2)
        print(f"v1: {self.getV1()} = {promedio1}")
        print(f"v2: {self.getV2()} = {promedio2}")
        if promedio1 > promedio2:
            print("¡El primero tiene un promedio mayor!")
        elif promedio1 < promedio2:
            print("¡El segundo tiene un promedio mayor!")
        else:
            print("¡Ambos vectores tienen promedios iguales!")

    # Mostrar inversos
    def mostrarInversos(self):
        print("")
        print("MOSTRAR INVERSOS")
        v1_inverso = []
        v2_inverso = []
        i = 0
        while i < len(self.getV1()):
            v1_inverso.append(self.getV1()[len(self.getV1()) - 1 - i])
            v2_inverso.append(self.getV2()[len(self.getV2()) - 1 - i])
            i = i + 1
        print(f"v1: {self.getV1()} = {v1_inverso}")
        print(f"v2: {self.getV2()} = {v2_inverso}")

    # Moda
    def moda(self):
        print("")
        print("MODA")

    # Tablas de multiplicar
    def tablasMultiplicar(self):
        print("")
        print("TABLAS DE MULTIPLICAR")
        # De v1
        j = 0
        while j < len(self.getV1()):
            i = 1
            while i < 11:
                print(f"v1: {self.getV1()[j]} x {i} = {self.getV1()[j] * i}")
                i = i + 1
            j = j + 1
            print("")
        # De v2
        j = 0
        while j < len(self.getV2()):
            i = 1
            while i < 11:
                print(f"v2: {self.getV2()[j]} x {i} = {self.getV2()[j] * i}")
                i = i + 1
            j = j + 1
            print("")
            
# Método principal de pruebas
def main():
    # Objeto 1
    tam = int(input("Ingrese el tamaño del vector: "))
    a = Vectores()
    a.llenarVector(tam)
    a.mostrarVector()
    """a.mostrarVectorInvertido()
    a.promedioElementosVector()
    a.mayorMenorVector()
    a.positivosNegativosVector()"""

    print("")

    # Objeto 2
    tam = int(input("Ingrese el tamaño del vector: "))
    b = Vectores()
    b.llenarVector(tam)
    b.mostrarVector()
    """b.mostrarVectorInvertido()
    b.promedioElementosVector()
    b.mayorMenorVector()
    b.positivosNegativosVector()"""

    operacion1 = OperadorVectores()
    operacion1.setV1(a.getVector())
    operacion1.setV2(b.getVector())
    operacion1.sumaPosicionesIguales()
    operacion1.sumaPosicionesInversas()
    operacion1.promedioMayor()
    operacion1.mostrarInversos()
    operacion1.moda()
    operacion1.tablasMultiplicar()

# Llamar método princial
main()