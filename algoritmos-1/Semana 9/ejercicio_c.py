# Ejercicio C

""" 
Un clase creadora de matrices, otra operadora de matrices

1) COMPARAR ELEMENTOS DIAGONAL PRINCIPAL
    - Mayor, menor, promedio
2) COMPARAR ELEMENTOS DE LA MATRIZ
    - Mayor, menor, promedio
3) COMPARAR ELEMENTOS DIAGONAL SECUNDARIA
    - Mayor, menor, promedio
"""

# Clase CREADORA de matrices
class Matrices():
    def __init__(self):
        self.__matriz = []

    def setMatriz(self, x:list):
        self.__matriz = x
    
    def getMatriz(self):
        return self.__matriz

    def llenarMatriz(self, indice:str, filas:int, columnas:int):
        print("")
        print(f"LLENAR MATRIZ {indice}")
        for i in range(filas):
            self.getMatriz().append([])
            for j in range(columnas):
                valor = int(input(f"Ingrese el elemento [{i}][{j}]: "))
                self.getMatriz()[i].append(valor)

    def mostrarMatriz(self, indice:str):
        print("")
        print(f"MATRIZ {indice}")
        filas = len(self.getMatriz())
        columnas = len(self.getMatriz()[0])
        for i in range(filas):
            print("[", end="")
            for j in range(columnas):
                if j != columnas - 1:
                    print(f"{self.getMatriz()[i][j]}", end=" ")
                else:
                    print(f"{self.getMatriz()[i][j]}", end="")
            print("]")

# Clase OPERADORA de matrices          
class OperadoraMatrices():
    def __init__(self):
        self.__parte1 = Matrices()
        self.__parte2 = Matrices()

    def setParte1(self, x:Matrices()):
        self.__parte1 = x
    
    def getParte1(self):
        return self.__parte1
    
    def setParte2(self, x:Matrices()):
        self.__parte2 = x
    
    def getParte2(self):
        return self.__parte2

    def compararDiagonalPincipal(self):
        print("")
        print("COMPARAR ELEMENTOS DIAGONAL PRINCIPAL")

        # Obtener diagonales principales
        filas = len(self.getParte1().getMatriz())
        columnas = len(self.getParte1().getMatriz()[0])
        dp_parte1 = []
        dp_parte2 = []
        for i in range(filas):
            for j in range(columnas):
                if i == j:
                    dp_parte1.append(self.getParte1().getMatriz()[i][j])
                    dp_parte2.append(self.getParte2().getMatriz()[i][j])

        # Mayor y menor
        mayor_dp_parte1 = dp_parte1[0]
        mayor_dp_parte2 = dp_parte2[0]
        menor_dp_parte1 = dp_parte1[0]
        menor_dp_parte2 = dp_parte2[0]
        for i in range(len(dp_parte1)):
            if dp_parte1[i] > mayor_dp_parte1:
                mayor_dp_parte1 = dp_parte1[i]
            if dp_parte1[i] < menor_dp_parte1:
                menor_dp_parte1 = dp_parte1[i]

            if dp_parte2[i] > mayor_dp_parte2:
                mayor_dp_parte2 = dp_parte2[i]
            if dp_parte2[i] < menor_dp_parte2:
                menor_dp_parte2 = dp_parte2[i]
        
        # Promedio
        sum_dp_parte1 = 0
        sum_dp_parte2 = 0
        for i in range(len(dp_parte1)):
            sum_dp_parte1 = sum_dp_parte1 + dp_parte1[i]
            sum_dp_parte2 = sum_dp_parte2 + dp_parte2[i]
        
        if len(dp_parte1) == 0:
            prom_dp_parte1 = 0
        else:
            prom_dp_parte1 = sum_dp_parte1 / len(dp_parte1)

        if len(dp_parte2) == 0:
            prom_dp_parte2 = 0
        else:
            prom_dp_parte2 = sum_dp_parte2 / len(dp_parte2)

        # Imprimir resultados
        print(f"Mayor parte 1: {mayor_dp_parte1}")
        print(f"Mayor parte 2: {mayor_dp_parte2}")
        print(f"Menor parte 1: {menor_dp_parte1}")
        print(f"Menor parte 2: {menor_dp_parte2}")
        print(f"Promedio parte 1: {prom_dp_parte1}")
        print(f"Promedio parte 2: {prom_dp_parte2}")

    def compararElementosMatriz(self):
        print("")
        print("COMPARAR ELEMENTOS MATRIZ")

        # Mayor y menor
        filas = len(self.getParte1().getMatriz())
        columnas = len(self.getParte1().getMatriz()[0])
        mayor_parte1 = self.getParte1().getMatriz()[0][0]
        mayor_parte2 = self.getParte2().getMatriz()[0][0]
        menor_parte1 = self.getParte1().getMatriz()[0][0]
        menor_parte2 = self.getParte2().getMatriz()[0][0]
        for i in range(filas):
            for j in range(columnas):
                if self.getParte1().getMatriz()[i][j] > mayor_parte1:
                    mayor_parte1 = self.getParte1().getMatriz()[i][j]
                if self.getParte1().getMatriz()[i][j] < menor_parte1:
                    menor_parte1 = self.getParte1().getMatriz()[i][j]

                if self.getParte2().getMatriz()[i][j] > mayor_parte2:
                    mayor_parte2 = self.getParte2().getMatriz()[i][j]
                if self.getParte2().getMatriz()[i][j] < menor_parte2:
                    menor_parte2 = self.getParte2().getMatriz()[i][j]

        # Promedio
        sum_parte1 = 0
        sum_parte2 = 0
        for i in range(filas):
            for j in range(columnas):
                sum_parte1 = sum_parte1 + self.getParte1().getMatriz()[i][j]
                sum_parte2 = sum_parte2 + self.getParte2().getMatriz()[i][j]
        
        cantidad_elementos = filas * columnas
 
        if cantidad_elementos == 0:
            prom_parte1 = 0
        else:
            prom_parte1 = sum_parte1 / cantidad_elementos

        if cantidad_elementos == 0:
            prom_parte2 = 0
        else:
            prom_parte2 = sum_parte2 / cantidad_elementos
        
        # Imprimir resultados
        print(f"Mayor parte 1: {mayor_parte1}")
        print(f"Mayor parte 2: {mayor_parte2}")
        print(f"Menor parte 1: {menor_parte1}")
        print(f"Menor parte 2: {menor_parte2}")
        print(f"Promedio parte 1: {prom_parte1}")
        print(f"Promedio parte 2: {prom_parte2}")

    def compararDiagonalSecundaria(self):
        print("")
        print("COMPARAR ELEMENTOS DIAGONAL SECUNDARIA")

        # Obtener diagonales secundarias
        filas = len(self.getParte1().getMatriz())
        columnas = len(self.getParte1().getMatriz()[0])
        ds_parte1 = []
        ds_parte2 = []
        for i in range(filas):
            for j in range(columnas):
                if i == j:
                    ds_parte1.append(self.getParte1().getMatriz()[i][columnas - 1 - j])
                    ds_parte2.append(self.getParte2().getMatriz()[i][columnas - 1 - j])

        # Mayor y menor
        mayor_ds_parte1 = ds_parte1[0]
        mayor_ds_parte2 = ds_parte2[0]
        menor_ds_parte1 = ds_parte1[0]
        menor_ds_parte2 = ds_parte2[0]
        for i in range(len(ds_parte1)):
            if ds_parte1[i] > mayor_ds_parte1:
                mayor_ds_parte1 = ds_parte1[i]
            if ds_parte1[i] < menor_ds_parte1:
                menor_ds_parte1 = ds_parte1[i]

            if ds_parte2[i] > mayor_ds_parte2:
                mayor_ds_parte2 = ds_parte2[i]
            if ds_parte2[i] < menor_ds_parte2:
                menor_ds_parte2 = ds_parte2[i]
        
        # Promedio
        sum_ds_parte1 = 0
        sum_ds_parte2 = 0
        for i in range(len(ds_parte1)):
            sum_ds_parte1 = sum_ds_parte1 + ds_parte1[i]
            sum_ds_parte2 = sum_ds_parte2 + ds_parte2[i]
        
        if len(ds_parte1) == 0:
            prom_ds_parte1 = 0
        else:
            prom_ds_parte1 = sum_ds_parte1 / len(ds_parte1)

        if len(ds_parte2) == 0:
            prom_ds_parte2 = 0
        else:
            prom_ds_parte2 = sum_ds_parte2 / len(ds_parte2)

        # Imprimir resultados
        print(f"Mayor parte 1: {mayor_ds_parte1}")
        print(f"Mayor parte 2: {mayor_ds_parte2}")
        print(f"Menor parte 1: {menor_ds_parte1}")
        print(f"Menor parte 2: {menor_ds_parte2}")
        print(f"Promedio parte 1: {prom_ds_parte1}")
        print(f"Promedio parte 2: {prom_ds_parte2}")

    # Suma
    def suma(self):
        print("")
        print("SUMA")
        filas = len(self.getParte1().getMatriz())
        columnas = len(self.getParte1().getMatriz()[0])
        matriz_nueva = []
        for i in range(filas):
            matriz_nueva.append([])
            for j in range(columnas):
                x = self.getParte1().getMatriz()[i][j] + self.getParte2().getMatriz()[i][j]
                matriz_nueva[i].append(x)
        
        for i in range(filas):
            print("[", end="")
            for j in range(columnas):
                if j != columnas - 1:
                    print(f"{matriz_nueva[i][j]}", end=" ")
                else:
                    print(f"{matriz_nueva[i][j]}", end="")
            print("]")

    # Resta
    def resta(self):
        print("")
        print("RESTA")
        filas = len(self.getParte1().getMatriz())
        columnas = len(self.getParte1().getMatriz()[0])
        matriz_nueva = []
        for i in range(filas):
            matriz_nueva.append([])
            for j in range(columnas):
                x = self.getParte1().getMatriz()[i][j] - self.getParte2().getMatriz()[i][j]
                matriz_nueva[i].append(x)
        
        for i in range(filas):
            print("[", end="")
            for j in range(columnas):
                if j != columnas - 1:
                    print(f"{matriz_nueva[i][j]}", end=" ")
                else:
                    print(f"{matriz_nueva[i][j]}", end="")
            print("]")

    # Producto
    def producto(self):
        print("")
        print("MULTIPLICACIÓN")
        
        m1 = self.getParte1().getMatriz()
        m2 = self.getParte2().getMatriz()

        # Procedimiento
        if len(m1[0]) == len(m2):
            # 1. Crear matriz nueva vacia con sus dimensiones
            m3 = []
            for i in range(len(m1)):
                m3.append([])
                for j in range(len(m2[0])):
                    m3[i].append(0)

            # 2. Calcular resultados
            for i in range(len(m1)):
                for j in range(len(m2[0])):

                    for k in range(len(m1[0])):
                        m3[i][j] = m3[i][j] + m1[i][k] * m2[k][j]

            # 3. Imprimir matriz nueva
            for i in range(len(m3)):
                print("[", end="")
                for j in range(len(m3[0])):
                    if j != len(m3[0]) - 1:
                        print(f"{m3[i][j]}", end=" ")
                    else:
                        print(f"{m3[i][j]}", end="")
                print("]")
        else:
           print("No se pueden multiplicar") 
    
    # División
    def division(self):
        print("")
        print("DIVISIÓN")
        filas = len(self.getParte1().getMatriz())
        columnas = len(self.getParte1().getMatriz()[0])
        matriz_nueva_1 = []
        matriz_nueva_2 = []
        dividendo_1 = int(input("Ingrese el dividendo para parte 1: "))
        dividendo_2 = int(input("Ingrese el dividendo para parte 2: "))

        while dividendo_1 == 0 or dividendo_2 == 0:
            print("Datos no válidos...")
            if dividendo_1 == 0:
                dividendo_1 = int(input("Ingrese el dividendo para parte 1: "))
            if dividendo_2 == 0:
                dividendo_2 = int(input("Ingrese el dividendo para parte 2: ")) 
        
        for i in range(filas):
            matriz_nueva_1.append([])
            matriz_nueva_2.append([])
            for j in range(columnas):
                x = round(self.getParte1().getMatriz()[i][j] / dividendo_1, 3)
                y = round(self.getParte2().getMatriz()[i][j] / dividendo_2, 3)
                matriz_nueva_1[i].append(x)
                matriz_nueva_2[i].append(y)
        
        print(f"Primera matriz dividida entre: {dividendo_1}")
        for i in range(filas):
                print("[", end="")
                for j in range(columnas):
                    if j != columnas - 1:
                        print(f"{matriz_nueva_1[i][j]}", end=" ")
                    else:
                        print(f"{matriz_nueva_1[i][j]}", end="")
                print("]")

        print(f"Segunda matriz dividida entre: {dividendo_2}")
        for i in range(filas):
                print("[", end="")
                for j in range(columnas):
                    if j != columnas - 1:
                        print(f"{matriz_nueva_2[i][j]}", end=" ")
                    else:
                        print(f"{matriz_nueva_2[i][j]}", end="")
                print("]")
        
# Método principal
def main():
    print("Ejercicio C")
    m1 = Matrices()
    #m1.setMatriz([[1,2,3],[4,5,6],[7,8,9]])
    m1.llenarMatriz("1", 3, 3)
    m1.mostrarMatriz("1")

    m2 = Matrices()
    #m2.setMatriz([[7,8,9],[4,5,6],[1,2,3]])
    m2.llenarMatriz("2", 3, 3)
    m2.mostrarMatriz("2")

    a = OperadoraMatrices()
    a.setParte1(m1)
    a.setParte2(m2)
    a.compararDiagonalPincipal()
    a.compararElementosMatriz()
    a.compararDiagonalSecundaria()
    a.suma()
    a.resta()
    a.producto()
    a.division()

# Llamar método principal
main()