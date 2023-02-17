# Tarea

# Clase para CREAR fracciones
class Fraccionarios():
    
    # Constructor
    def __init__(self):
        # Atributos por defecto...
        self.numerador = 0
        self.denominador = 0

    # set() ALMACENAR
    def setNumerador(self, x:int): # variable:tipo
        self.numerador = x

    def setDenominador(self, x:int):
        self.denominador = x

    # get() MOSTRAR
    def getNumerador(self):
        return self.numerador

    def getDenominador(self):
        return self.denominador

# Clase para OPERAR fracciones
class CalculadoraFraccionarios():
    
    # Constructor
    def __init__(self):
        self.parte1 = Fraccionarios()
        self.parte2 = Fraccionarios()

    # set() ALMACENAR
    def setParte1(self, x:Fraccionarios()):
        self.parte1 = x

    def setParte2(self, x:Fraccionarios()):
        self.parte2 = x

    # get() MOSTRAR
    def getParte1(self):
        return self.parte1

    def getParte2(self):
        return self.parte2

    # Suma heterogéna
    def sumaHeterogena(self):
        numerador = (self.parte1.getNumerador() * self.parte2.getDenominador()) + (self.parte1.getDenominador() * self.parte2.getNumerador())
        denominador = self.parte1.getDenominador() * self.parte2.getDenominador()
        print(f"{numerador} / {denominador} = {round(numerador / denominador,2)}")

    # Suma homogéna
    def sumaHomogenea(self):
        numerador = self.parte1.getNumerador() + self.parte2.getNumerador()
        denominador = self.parte1.getDenominador()
        print(f"{numerador} / {denominador} = {round(numerador / denominador,2)}")

    # Resta normal
    def restaNormal(self):
        numerador = (self.parte1.getNumerador() * self.parte2.getDenominador()) - (self.parte1.getDenominador() * self.parte2.getNumerador())
        denominador = self.parte1.getDenominador() * self.parte2.getDenominador()
        print(f"{numerador} / {denominador} = {round(numerador / denominador,2)}")

    # Multiplicación normal
    def multiplicacionNormal(self):
        numerador = self.parte1.getNumerador() * self.parte2.getNumerador()
        denominador = self.parte1.getDenominador() * self.parte2.getDenominador()
        print(f"{numerador} / {denominador} = {round(numerador / denominador,2)}")

# Método principal para pruebas
def main():
    
    print("SUMA HETEROGÉNEA")
    # Fracción 1
    f1 = Fraccionarios()
    f1.setNumerador(1)
    f1.setDenominador(5)

    # Fracción 2
    f2 = Fraccionarios()
    f2.setNumerador(1)
    f2.setDenominador(6)

    print(f"Fracción 1: {f1.getNumerador()} / {f1.getDenominador()}")
    print(f"Fracción 2: {f2.getNumerador()} / {f2.getDenominador()}")
    
    operacion1 = CalculadoraFraccionarios()
    operacion1.setParte1(f1)
    operacion1.setParte2(f2)
    operacion1.sumaHeterogena()

    print("")
    print("SUMA HOMOGÉNEA")
    # Fracción 3
    f3 = Fraccionarios()
    f3.setNumerador(4)
    f3.setDenominador(6)

    # Fracción 4
    f4 = Fraccionarios()
    f4.setNumerador(7)
    f4.setDenominador(6)

    print(f"Fracción 3: {f3.getNumerador()} / {f3.getDenominador()}")
    print(f"Fracción 4: {f4.getNumerador()} / {f4.getDenominador()}")

    operacion2 = CalculadoraFraccionarios()
    operacion2.setParte1(f3)
    operacion2.setParte2(f4)
    operacion2.sumaHomogenea()

    print("")
    print("RESTA NORMAL")
    # Fracción 5
    f5 = Fraccionarios()
    f5.setNumerador(1)
    f5.setDenominador(5)

    # Fracción 6
    f6 = Fraccionarios()
    f6.setNumerador(1)
    f6.setDenominador(6)

    print(f"Fracción 5: {f5.getNumerador()} / {f5.getDenominador()}")
    print(f"Fracción 6: {f6.getNumerador()} / {f6.getDenominador()}")

    operacion3 = CalculadoraFraccionarios()
    operacion3.setParte1(f5)
    operacion3.setParte2(f6)
    operacion3.restaNormal()

    print("")
    print("MULTIPLICACIÓN NORMAL")
    # Fracción 7
    f7 = Fraccionarios()
    f7.setNumerador(8)
    f7.setDenominador(10)

    # Fracción 8
    f8 = Fraccionarios()
    f8.setNumerador(2)
    f8.setDenominador(3)

    print(f"Fracción 7: {f7.getNumerador()} / {f7.getDenominador()}")
    print(f"Fracción 8: {f8.getNumerador()} / {f8.getDenominador()}")

    operacion4 = CalculadoraFraccionarios()
    operacion4.setParte1(f7)
    operacion4.setParte2(f8)
    operacion4.multiplicacionNormal()

# Llamar método principal para pruebas
main()