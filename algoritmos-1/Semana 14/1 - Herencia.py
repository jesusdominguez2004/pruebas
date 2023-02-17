class Padre:
    def __init__(self) -> None:
        self.nombre = None
        self.apellido = None

    def set_nombre(self, nombre:str):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre

    def set_apellido(self, apellido:str):
        self.apellido = apellido

    def get_apellido(self):
        return self.apellido

    def imprimir(self) -> str:
        print(f"{self.nombre} {self.apellido}")

class Hijo(Padre):
    def __init__(self) -> None:
        # Hijo hereda constructor clase padre
        super().__init__()
        # self.nombre = None
        # self.apellido = None
        self.edad = None

    def set_edad(self, edad:int):
        self.edad = edad

    def get_edad(self):
        return self.edad

    def imprimir(self) -> str:
        # Hijo hereda método imprimir clase padre
        super().imprimir()
        print(self.edad)

def main():
    padre = Padre()
    padre.set_nombre("Deiner")
    padre.set_apellido("Domínguez")
    padre.imprimir()

    hijo = Hijo()
    hijo.set_nombre("Jesús")
    hijo.set_apellido("Domínguez")
    hijo.set_edad(18)
    hijo.imprimir()

main()