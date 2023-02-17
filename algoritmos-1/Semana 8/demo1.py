# Semana 8 | Algoritmos I


"""
SOBRECARGA o POLIMORFISMO: Definir objetos bajo un mismo nombre
pero con diferentes parámetros (o init's).

En función del PARÁMETRO, elige cuál COSTRUCTOR ejecutar...
    init()
    init(int)
    init(float)
    init(fracciones)
    init([])
    init([][])

En función del PARÁMETRO, elige cuál MÉTODO ejecutar...
    sumarFracciones()
    sumarFracciones(int)
    sumarFracciones(float)
    sumarFracciones(fracciones)
    sumarFracciones([])
    sumarFracciones([][])

SOBRE_ESCRITURA: 
"""

# Crear clase personas
class Personas():

    # Constructor (otra forma de hacerlo, usando parámetros)
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido

    # Set() and Get()
    def setNombre(self, nombre:str):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido:str):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

    def saludar(self):
        print(f"¡Hola {self.getNombre()} {self.getApellido()}!")

# Método principal
def main():

    # Persona 1 (SIN USAR SET)
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese el apellido: ")
    p1 = Personas(nombre, apellido)
    p1.saludar()
    
# Llamar método principal
main()