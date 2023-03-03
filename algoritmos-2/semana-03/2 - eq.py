class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"Soy {self.nombre}\ntengo {self.edad} años"

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Persona):
            return False
        return self.nombre == __o.nombre


persona_1 = Persona("Jesús", 18)
persona_2 = Persona("Jesús", 10)
persona_3 = Persona("Santiago", 10)
print(persona_1 == persona_2)
print(persona_1 == persona_3)
