# INDICADOR 1: Ejemplo de herencia y polimorfismo (sobreescitura de métodos) 

# Personas
class Personas:
    def __init__(self) -> None:
        self.__nombre = None
        self.__apellido = None
        self.__edad = None

    def set_nombre(self, nombre:str) -> None:
        self.__nombre = nombre

    def get_nombre(self) -> str:
        return self.__nombre

    def set_apellido(self, apellido:str) -> None:
        self.__apellido = apellido

    def get_apellido(self) -> str:
        return self.__apellido

    def set_edad(self, edad:int) -> None:
        self.__edad = edad

    def get_edad(self) -> int:
        return self.__edad

    def saludar(self) -> str:
        print(f"Hola, soy {self.get_nombre()} {self.get_apellido()}, tengo {self.get_edad()} años")

# Estudiantes
class Estudiantes(Personas):
    def __init__(self) -> None:
        super().__init__()
        self.sede = None
        self.materias = None

    def set_sede(self, sede:str) -> None:
        self.__sede = sede

    def get_sede(self) -> str:
        return self.__sede

    def set_materias(self, materias:int) -> None:
        self.__materias = materias

    def get_materias(self) -> int:
        return self.__materias

    def saludar(self) -> str:
        super().saludar()
        print(f"Soy un estudiante de {self.get_sede()}")
        print(f"Y tengo {self.get_materias()} materias")

# Empleados
class Empleados(Personas):
    def __init__(self) -> None:
        super().__init__()
        self.empresa = None
        self.salario = None

    def set_empresa(self, empresa:str) -> None:
        self.__empresa = empresa

    def get_empresa(self) -> str:
        return self.__empresa

    def set_salario(self, salario:int) -> None:
        self.__salario = salario

    def get_salario(self) -> int:
        return self.__salario 

    def saludar(self) -> str:
        super().saludar()
        print(f"Trabajo en {self.get_empresa()}")
        print(f"Y tengo un salario de ${self.get_salario():,}")

# Método principal
def main():
    persona_1 = Personas()
    persona_1.set_nombre("Deiner")
    persona_1.set_apellido("Domínguez")
    persona_1.set_edad(42)
    persona_1.saludar()

    print("")
    estudiante_1 = Estudiantes()
    estudiante_1.set_nombre("Jesús")
    estudiante_1.set_apellido("Domínguez")
    estudiante_1.set_edad(18)
    estudiante_1.set_sede("Universidad de la Costa")
    estudiante_1.set_materias(50)
    estudiante_1.saludar()

    print("")

    empleado_1 = Empleados()
    empleado_1.set_nombre("Santiago")
    empleado_1.set_apellido("Domínguez")
    empleado_1.set_edad(25)
    empleado_1.set_empresa("Google")
    empleado_1.set_salario(5450000)
    empleado_1.saludar()

# Llamar método principal
main()