class Persona:

    def __init__(self, nombre, apellido, documento):
        self.nombre    = nombre
        self.apellido  = apellido
        self.documento = documento

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_documento(self, documento):
        self.documento = documento

    def get_nombre(self):
        return self.nombre 

    def get_apellido(self):
        return self.apellido 

    def get_documento(self):
        return self.documento 


class Profesor(Persona):

    def __init__(self, nombre, apellido, documento, tipo_contrato):
        super().__init__(nombre, apellido, documento)
        self.tipo_contrato = tipo_contrato

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.documento} {self.tipo_contrato}"

class Universidad:
     
     def __init__(self, nombre_universidad):  
        self.nombre_universidad = nombre_universidad 
        self.profesores = []     

     def agregarProfesor(self, profesor):
        self.profesores.append(profesor) 

     def listar(self):
        return self.profesores
        
pro1 = Profesor("JUAN", "PEREZ" ,76665 , "INDEFINIDO")
pro2 = Profesor("LAURA", "ACUÑA" ,112233 , "PRESTACION DE SERVICIOS")
u1 = Universidad("UNIVERSIDAD DE LA COSTA")
u1.agregarProfesor(pro1)
u1.agregarProfesor(pro2)
listado = u1.listar()

for item in listado:
    print(item)