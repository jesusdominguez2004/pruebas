class Coche: # nombre/identificador clase
    """Docstring -> Esta clase define el estado y comportamiento de un coche"""
    
    ruedas = 4 # atributo de clase

    # constructor
    def __init__(self, color, aceleracion):
        # atributos de instancia
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    # métodos
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        v = self.velocidad - self.aceleracion
        if v < 0: 
            v = 0
        self.velocidad = v

# Instanciar/crear objetos
c1 = Coche('rojo', 20)
c2 = Coche('azul', 20)
print(c1.color) # Atributo de instancia
print(c2.color) # Atributo de instancia

print(c1.ruedas) # Atributo de clase (4)
print(c2.ruedas) # Atributo de clase (4)
Coche.ruedas = 6
print(c1.ruedas) # Atributo de clase (6)
print(c2.ruedas) # Atributo de clase (6)



