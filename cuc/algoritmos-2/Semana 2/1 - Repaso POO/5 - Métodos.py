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
c1.acelera() # Forma 1
Coche.acelera(c2) # Forma 2
print(c1.velocidad) # 20
print(c2.velocidad) # 20

print(Coche.acelera) # Función de clase
print(c1.acelera) # Método del objeto
