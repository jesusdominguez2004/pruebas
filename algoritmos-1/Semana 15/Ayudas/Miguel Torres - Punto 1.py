class Animales:
    def __init__(self):
        self.especie = "" #
        self.dieta = ""

    def set_especie(self, x:str):
        self.especie = x

    def get_especie(self):
        return self.especie

    def set_dieta(self, x:str):
        self.dieta = x

    def get_dieta(self):
        return self.dieta

    def imprimir(self):
        print("Especie:", self.get_especie())
        print("Dieta:", self.get_dieta())
        
class Mascotas(Animales):
    def __init__(self):
        super().__init__()
        self.nombre = ""

    def set_nombre(self, x:str):
        self.nombre = x

    def get_nombre(self):
        return self.nombre 

    def imprimir(self):
        super().imprimir()
        print("Nombre mascota:", self.get_nombre())

def main():
    print("Objeto clase padre ANIMALES")
    animal_1 = Animales()
    animal_1.set_especie('Canis familiaris')
    animal_1.set_dieta('Omnívoro')
    animal_1.imprimir()
    
    print("\n")

    print("Objeto clase hijo MASCOTAS")
    mascota_1 = Mascotas()
    mascota_1.set_especie('Felis Silvestris Catus')
    mascota_1.set_dieta('Carnívoro')
    mascota_1.set_nombre('Germán')
    mascota_1.imprimir()

main()