# Otro ejemplo de herencia
# Polimorfismo por sobreescribir
# Varias subclases heredan métodos y atributos de la super clase

class Personas:
    def __init__(self) -> None:
        self.nombre = None
        self.apellido = None
        self.id = None
        self.edad = None
        self.correo = None

    def set_nombre(self, x:str): 
        self.nombre = x

    def get_nombre(self) -> str: 
        return self.nombre

    def set_apellido(self, x:str):
        self.apellido = x

    def get_apellido(self) -> str: 
        return self.apellido

    def set_id(self, x:int): 
        self.id = x

    def get_id(self) -> int: 
        return self.id

    def set_edad(self, x:int): 
        self.edad = x

    def get_edad(self) -> int: 
        return self.edad

    def set_correo(self, x:str): 
        self.correo = x

    def get_correo(self) -> str: 
        return self.correo

    def imprimir_datos(self) -> str:
        print(f"NOMBRE: {self.get_nombre()} {self.get_apellido()}")
        print(f"ID: {self.get_id()}")
        print(f"EDAD: {self.get_edad()}")
        print(f"CORREO: {self.get_correo()}")

class Empleados(Personas):
    def __init__(self) -> None:
        super().__init__()
        self.cargo = None
        self.antiguedad = None
        self.profesion = None

    def set_cargo(self, x:str):
        self.cargo = x

    def get_cargo(self) -> str: 
        return self.cargo

    def set_antiguedad(self, x:int):
        self.antiguedad = x

    def get_antiguedad(self) -> int: 
        return self.antiguedad

    def set_profesion(self, x:str):
        self.profesion = x

    def get_profesion(self) -> str: 
        return self.profesion

    def imprimir_datos(self) -> str:
        super().imprimir_datos()
        print(f"CARGO: {self.get_cargo()}")
        print(f"ANTIGÜEDAD: {self.get_antiguedad()}")
        print(f"PROFESIÓN: {self.get_profesion()}")

class TiempoCompleto(Empleados):
    def __init__(self) -> None:
        super().__init__()
        self.horas = None
        self.area = None # "Software" "Redes" "TIC"

    def set_horas(self, x:int):
        self.horas = x

    def get_horas(self) -> int: 
        return self.horas

    def set_area(self, x:str):
        self.area = x

    def get_area(self) -> str: 
        return self.area

    def imprimir_datos(self) -> str:
        super().imprimir_datos()
        print(f"HORAS: {self.get_horas()}")
        print(f"ÁREA DE FORMACIÓN: {self.get_area()}")

class PorLabor(Empleados):
    def __init__(self) -> None:
        super().__init__()  
        self.labor = None
        self.fecha_inicio = None
        self.fecha_finalizacion = None

    def set_labor(self, x:str):
        self.labor = x

    def get_labor(self) -> str: 
        return self.labor

    def set_fecha_inicio(self, x:str):
        self.fecha_inicio = x

    def get_fecha_inicio(self) -> str: 
        return self.fecha_inicio
    
    def set_fecha_finalizacion(self, x:str):
        self.fecha_finalizacion = x

    def get_fecha_finalizacion(self) -> str: 
        return self.fecha_finalizacion

    def imprimir_datos(self) -> str:
        super().imprimir_datos()
        print(f"LABOR: {self.get_labor()}")
        print(f"FECHA INICIO: {self.get_fecha_inicio()}")
        print(f"FECHA FINALIZACIÓN: {self.get_fecha_finalizacion()}")

class Estudiantes(Personas):
    def __init__(self) -> None:
        super().__init__()
        self.institucion = None
        self.materia_favorita = None

    def set_institucion(self, x:str):
        self.institucion = x

    def get_institucion(self) -> str: 
        return self.institucion

    def set_materia_favorita(self, x:str):
        self.materia_favorita = x

    def get_materia_favorita(self) -> str: 
        return self.materia_favorita

    def imprimir_datos(self) -> str:
        super().imprimir_datos()
        print(f"INSTITUCIÓN: {self.get_institucion()}")
        print(f"MATERIA FAVORITA: {self.get_materia_favorita()}")

class Secundaria(Estudiantes):
    def __init__(self) -> None:
        super().__init__()
        self.director_grupo = None
        self.grado = None
    
    def set_director_grupo(self, x:str):
        self.director_grupo = x

    def get_director_grupo(self) -> str: 
        return self.director_grupo
    
    def set_grado(self, x:str):
        self.grado = x

    def get_grado(self) -> str: 
        return self.grado

    def imprimir_datos(self) -> str:
        super().imprimir_datos()
        print(f"DIRECTOR GRUPO: {self.get_director_grupo()}")
        print(f"GRADO: {self.get_grado()}")

class Universitario(Estudiantes):
    def __init__(self) -> None:
        super().__init__()
        self.carrera = None
        self.semestres = None
        self.creditos = None

    def set_carrera(self, x:str):
        self.carrera = x

    def get_carrera(self) -> str: 
        return self.carrera

    def set_semestres(self, x:int):
        self.semestres = x

    def get_semestres(self) -> int: 
        return self.semestres

    def set_creditos(self, x:int):
        self.creditos = x

    def get_creditos(self) -> int: 
        return self.creditos

    def imprimir_datos(self) -> str:
        super().imprimir_datos()
        print(f"CARRERA: {self.get_carrera()}")
        print(f"SEMESTRES: {self.get_semestres()}")
        print(f"CRÉDITOS: {self.get_creditos()}")

# Método principal
def main():
    ejemplo_1 = Personas()
    ejemplo_1.set_nombre("Deiner")
    ejemplo_1.set_apellido("Domínguez")
    ejemplo_1.set_id(123)
    ejemplo_1.set_edad(42)
    ejemplo_1.set_correo("ejemplo1@gmail.com")
    ejemplo_1.imprimir_datos()
    print("")

    ejemplo_2 = Empleados()
    ejemplo_2.set_nombre("Elvia")
    ejemplo_2.set_apellido("Cristina")
    ejemplo_2.set_id(456)
    ejemplo_2.set_edad(39)
    ejemplo_2.set_correo("ejemplo2@gmail.com")
    ejemplo_2.set_cargo("Limpieza facial")
    ejemplo_2.set_antiguedad(2009)
    ejemplo_2.set_profesion("Cosmetología")
    ejemplo_2.imprimir_datos()
    print("")

    ejemplo_3 = TiempoCompleto()
    ejemplo_3.set_nombre("Santiago")
    ejemplo_3.set_apellido("Domínguez")
    ejemplo_3.set_id(789)
    ejemplo_3.set_edad(11)
    ejemplo_3.set_correo("ejemplo3@gmail.com")
    ejemplo_3.set_cargo("Desarrollador FrontEnd")
    ejemplo_3.set_antiguedad(2010)
    ejemplo_3.set_profesion("Ingeniería de sistema")
    ejemplo_3.set_horas(144)
    ejemplo_3.set_area("Software")
    ejemplo_3.imprimir_datos()
    print("")

    ejemplo_4 = PorLabor()
    ejemplo_4.set_nombre("Jesús")
    ejemplo_4.set_apellido("Domínguez")
    ejemplo_4.set_id(1044)
    ejemplo_4.set_edad(18)
    ejemplo_4.set_correo("ejemplo4@gmail.com")
    ejemplo_4.set_cargo("Desarrollador BackEnd")
    ejemplo_4.set_antiguedad(2021)
    ejemplo_4.set_profesion("Ingeniería de sistema")
    ejemplo_4.set_labor("CRUD Base de datos")
    ejemplo_4.set_fecha_inicio("12-11-2022")
    ejemplo_4.set_fecha_finalizacion("31-12-2022")
    ejemplo_4.imprimir_datos()
    print("")

    ejemplo_5 = Estudiantes()
    ejemplo_5.set_nombre("Esteban")
    ejemplo_5.set_apellido("Jiménez")
    ejemplo_5.set_id(1423)
    ejemplo_5.set_edad(22)
    ejemplo_5.set_correo("ejemplo5@gmail.com")
    ejemplo_5.set_institucion("IETECI")
    ejemplo_5.set_materia_favorita("Informática")
    ejemplo_5.imprimir_datos()
    print("")

    ejemplo_6 = Secundaria()
    ejemplo_6.set_nombre("Alfonso")
    ejemplo_6.set_apellido("Charris")
    ejemplo_6.set_id(1273)
    ejemplo_6.set_edad(15)
    ejemplo_6.set_correo("ejemplo6@gmail.com")
    ejemplo_6.set_institucion("INEM")
    ejemplo_6.set_materia_favorita("Historia")
    ejemplo_6.set_director_grupo("Nelson Cruz")
    ejemplo_6.set_grado(11)
    ejemplo_6.imprimir_datos()
    print("")

    ejemplo_7 = Universitario()
    ejemplo_7.set_nombre("Samuel")
    ejemplo_7.set_apellido("Fontalvo")
    ejemplo_7.set_id(1212)
    ejemplo_7.set_edad(30)
    ejemplo_7.set_correo("ejemplo7@gmail.com")
    ejemplo_7.set_institucion("Universidad de la Costa")
    ejemplo_7.set_materia_favorita("Algoritmos 1")
    ejemplo_7.set_carrera("Ingeniería de sistemas")
    ejemplo_7.set_semestres(10)
    ejemplo_7.set_creditos(160)
    ejemplo_7.imprimir_datos()

# Llamar método principal
main()