class Matriz():
    # Constructor
    def __init__(self):
        self.matriz = []

    # Set()
    def setMatriz(self, matriz:list):
        self.matriz = matriz

    # Get()
    def getMatriz(self):
        return self.matriz

    # Llenar matriz
    def llenarMatriz(self, filas:int, columnas:int):
        for i in range(filas):
            self.getMatriz().append([])
            for j in range(columnas):
                elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))
                self.getMatriz()[i].append(elemento)
        print("Proceso Exitoso...")
    
    # Mostrar matriz
    def mostrarMatriz(self):
        # Filas
        for i in range(len(self.getMatriz())):
            # Columnas
            for j in range(len(self.getMatriz()[0])):
                print(f"Matriz [{i}][{j}] = {self.getMatriz()[i][j]}")

# Método principal
def main():
    matriz1 = Matriz()
    filas = int(input("Ingrese número de filas: "))
    columnas = int(input("Ingrese número de columnas: "))
    matriz1.llenarMatriz(filas, columnas)
    matriz1.mostrarMatriz()

# Llamar método principal
main()