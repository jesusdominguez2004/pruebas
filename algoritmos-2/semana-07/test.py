# Prueba de "Error Lens"

class Personas:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad 
    
    def __str__(self) -> str:
        return f"¡Soy {self.nombre} y tengo {self.edad} años!"


persona_1 = Personas("Jesús", 18)
persona_2 = Personas("Santiago", 12)
print(persona_1, persona_2, sep="\n")
