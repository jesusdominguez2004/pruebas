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
print(c1.color) # atributo
print(c1.velocidad) # atributo
c1.acelera() # método
print(c1.velocidad) # atributo
