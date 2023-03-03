class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"Soy {self.nombre}\ntengo {self.edad} años"


persona_1 = Persona("Jesús", 18)
print(persona_1)
