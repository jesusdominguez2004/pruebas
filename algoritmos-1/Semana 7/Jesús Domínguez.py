# Calculadora fracciones | Jesús Domínguez

# Clase creadora de fracciones
class Fraccionarios():
    
    # Constructor
    def __init__(self):
        # Atributos por defecto
        self.numerador = 0
        self.denominador = 0

    # Set()
    def setNumerador(self, x:int):
        self.numerador = x

    def setDenominador(self, x:int):
        self.denominador = x

    # Get()
    def getNumerador(self):
        return self.numerador

    def getDenominador(self):
        return self.denominador

# Clase operadora de fracciones
class CalculadoraFraccionarios():
    
    # Constructor
    def __init__(self):
        # f1 y f2 son atributos
        # del objeto cálculo
        self.f1 = Fraccionarios()
        self.f2 = Fraccionarios()

    # Set()
    def setF1(self, x:Fraccionarios()):
        self.f1 = x

    def setF2(self, x:Fraccionarios()):
        self.f2 = x

    # Get()
    def getF1(self):
        return self.f1

    def getF2(self):
        return self.f2
        
    # Suma HETEROGÉNEA
    def sumaFraccionesHeterogeneas(self):
        numerador = (self.f1.getNumerador() * self.f2.getDenominador()) + (self.f1.getDenominador() * self.f2.getNumerador())
        denominador = self.f1.getDenominador() * self.f2.getDenominador()
        print(f"{numerador} / {denominador} = {round(numerador / denominador, 2)}")

    # Suma HOMOGÉNEAS
    def sumaFraccionesHomogeneas(self):
        numerador = self.f1.getNumerador() + self.f2.getNumerador()
        denominador = self.f1.getDenominador()
        print(f"{numerador} / {denominador} = {round(numerador / denominador, 2)}")

    # Resta HETEROGÉNEA
    def restaFraccionesHeterogeneas(self):
        numerador = (self.f1.getNumerador() * self.f2.getDenominador()) - (self.f1.getDenominador() * self.f2.getNumerador())
        denominador = self.f1.getDenominador() * self.f2.getDenominador()
        print(f"{numerador} / {denominador} = {round(numerador / denominador, 2)}")

    # Resta HOMOGÉNEAS
    def restaFraccionesHomogeneas(self):
        numerador = self.f1.getNumerador() - self.f2.getNumerador()
        denominador = self.f1.getDenominador()
        print(f"{numerador} / {denominador} = {round(numerador / denominador, 2)}")

    # Multiplicación
    def multiplicacionFracciones(self):
        numerador = self.f1.getNumerador() * self.f2.getNumerador()
        denominador = self.f1.getDenominador() * self.f2.getDenominador()
        print(f"{numerador} / {denominador} = {round(numerador / denominador, 2)}")

    # División
    def divisionFracciones(self):
        numerador = self.f1.getNumerador() * self.f2.getDenominador()
        denominador = self.f1.getDenominador() * self.f2.getNumerador()
        print(f"{numerador} / {denominador} = {round(numerador / denominador, 2)}")


# Método principal para pruebas
def main():

    print("- - SUMA HETEROGÉNEA - -")
    # Fracción 1
    f1 = Fraccionarios()   # Instancia de clase
    f1.setNumerador(10)    # Asignar atributo
    f1.setDenominador(20)  # Asignar atributo

    # Fracción 2
    f2 = Fraccionarios()   # Instancia de clase
    f2.setNumerador(30)    # Asignar atributo
    f2.setDenominador(40)  # Asignar atributo

    # Imprimir
    print(f"Fracción 1: {f1.getNumerador()} / {f1.getDenominador()}")
    print(f"Fracción 2: {f2.getNumerador()} / {f2.getDenominador()}")

    # Suma heterogénea
    calculo1 = CalculadoraFraccionarios()
    calculo1.setF1(f1)
    calculo1.setF2(f2)
    calculo1.sumaFraccionesHeterogeneas()

    print("- - SUMA HOMOGÉNEA - -")
    # Fracción 3
    f3 = Fraccionarios()   # Instancia de clase
    f3.setNumerador(3)    # Asignar atributo
    f3.setDenominador(10)  # Asignar atributo

    # Fracción 4
    f4 = Fraccionarios()   # Instancia de clase
    f4.setNumerador(5)    # Asignar atributo
    f4.setDenominador(10)  # Asignar atributo

    # Imprimir
    print(f"Fracción 3: {f3.getNumerador()} / {f3.getDenominador()}")
    print(f"Fracción 4: {f4.getNumerador()} / {f4.getDenominador()}")

    # Suma homogénea
    calculo2 = CalculadoraFraccionarios()
    calculo2.setF1(f3)
    calculo2.setF2(f4)
    calculo2.sumaFraccionesHomogeneas()

    print("- - RESTA HETEROGÉNEA - -")
    # Fracción 5
    f5 = Fraccionarios()   # Instancia de clase
    f5.setNumerador(4)    # Asignar atributo
    f5.setDenominador(7)  # Asignar atributo

    # Fracción 6
    f6 = Fraccionarios()   # Instancia de clase
    f6.setNumerador(2)    # Asignar atributo
    f6.setDenominador(5)  # Asignar atributo

    # Imprimir
    print(f"Fracción 5: {f5.getNumerador()} / {f5.getDenominador()}")
    print(f"Fracción 6: {f6.getNumerador()} / {f6.getDenominador()}")

    # Resta heterogénea
    calculo3 = CalculadoraFraccionarios()
    calculo3.setF1(f5)
    calculo3.setF2(f6)
    calculo3.restaFraccionesHeterogeneas()

    print("- - RESTA HOMOGÉNEA - -")
    # Fracción 7
    f7 = Fraccionarios()   # Instancia de clase
    f7.setNumerador(10)    # Asignar atributo
    f7.setDenominador(45)  # Asignar atributo

    # Fracción 8
    f8 = Fraccionarios()   # Instancia de clase
    f8.setNumerador(20)    # Asignar atributo
    f8.setDenominador(45)  # Asignar atributo

    # Imprimir
    print(f"Fracción 7: {f7.getNumerador()} / {f7.getDenominador()}")
    print(f"Fracción 8: {f8.getNumerador()} / {f8.getDenominador()}")

    # Resta homogénea
    calculo4 = CalculadoraFraccionarios()
    calculo4.setF1(f7)
    calculo4.setF2(f8)
    calculo4.restaFraccionesHomogeneas()

    print("- - MULTIPLICACIÓN - -")
    # Fracción 9
    f9 = Fraccionarios()   # Instancia de clase
    f9.setNumerador(9)    # Asignar atributo
    f9.setDenominador(12)  # Asignar atributo

    # Fracción 10
    f10 = Fraccionarios()   # Instancia de clase
    f10.setNumerador(2)    # Asignar atributo
    f10.setDenominador(2)  # Asignar atributo

    # Imprimir
    print(f"Fracción 9: {f9.getNumerador()} / {f9.getDenominador()}")
    print(f"Fracción 10: {f10.getNumerador()} / {f10.getDenominador()}")

    # Multiplicación
    calculo5 = CalculadoraFraccionarios()
    calculo5.setF1(f9)
    calculo5.setF2(f10)
    calculo5.multiplicacionFracciones()

    print("- - DIVISIÓN - -")
    # Fracción 11
    f11 = Fraccionarios()   # Instancia de clase
    f11.setNumerador(12)    # Asignar atributo
    f11.setDenominador(9)  # Asignar atributo

    # Fracción 12
    f12 = Fraccionarios()   # Instancia de clase
    f12.setNumerador(2)    # Asignar atributo
    f12.setDenominador(5)  # Asignar atributo

    # Imprimir
    print(f"Fracción 11: {f11.getNumerador()} / {f11.getDenominador()}")
    print(f"Fracción 12: {f12.getNumerador()} / {f12.getDenominador()}")

    # División
    calculo6 = CalculadoraFraccionarios()
    calculo6.setF1(f11)
    calculo6.setF2(f12)
    calculo6.divisionFracciones()

# Llamar método principal de pruebas
main()