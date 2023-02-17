# Indicador 2 | Jesús Domínguez

class Cliente():
    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__identificacion = None
        self.__telefono = None
        self.__email = None
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
       return self.__nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_apellido(self):
       return self.__apellido

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    def get_identificacion(self):
       return self.__identificacion
    
    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_telefono(self):
       return self.__telefono

    def set_email(self, email):
        self.__email = email

    def get_email(self):
       return self.__email

class Paquetes():
    def __init__(self):
        self.__id_paquete = None
        self.__peso = None
        self.__fragil = None
    
    def set_id_paquete(self, id_paquete):
        self.__id_paquete = id_paquete

    def get_id_paquete(self):
       return self.__id_paquete

    def set_peso(self, peso):
        self.__peso = peso

    def get_peso(self):
       return self.__peso
       
    def set_fragil(self, fragil):
        self.__fragil = fragil

    def get_fragil(self):
       return self.__fragil

class Venta(Cliente, Paquetes):
    def __init__(self):
        self.__id_venta = None
        self.__fecha = None
        self.__valor_kg = None
        self.__valor_envio = None
    
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def get_id_venta(self):
       return self.__id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def get_fecha(self):
       return self.__fecha
       
    def set_valor_kg(self, valor_kg):
        self.__valor_kg = valor_kg

    def get_valor_kg(self):
       return self.__valor_kg

    def set_valor_envio(self, valor_envio):
        self.__valor_envio = valor_envio

    def get_valor_envio(self):
       return self.__valor_envio

    def crear_venta(self):
        print("CREAR VENTA")
        id_venta = int(input("Ingrese ID VENTA: "))
        fecha = input("Ingrese FECHA: ")
        nombre  = input("Ingrese NOMBRE: ")
        apellido = input("Ingrese APELLIDO: ")
        telefono = input("Ingrese TELÉFONO: ")
        email = input("Ingrese EMAIL: ")
        identificacion = int(input("Ingrese IDENTIFICACIÓN: "))
        id_paquete = int(input("Ingrese ID PAQUETE: "))
        fragil = int(input("Ingrese FRAGILIDAD PAQUETE 1 = Sí, 2 = No: "))
        while fragil != 1 and fragil != 2:
            print("Datos no válidos...")
            fragil = int(input("Ingrese FRAGILIDAD PAQUETE 1 = Sí, 2 = No: "))
        if fragil == 1:
            fragil = "Sí"
        else:
            fragil = "No"
        peso = eval(input("Ingrese PESO (KG): "))
        valor_kg = eval(input("Ingrese VALOR KILO: $"))
        valor_envio = peso * valor_kg

        self.set_id_venta(id_venta)
        self.set_fecha(fecha)

        self.set_nombre(nombre)
        self.set_apellido(apellido)
        self.set_identificacion(identificacion)
        self.set_telefono(telefono)
        self.set_email(email)
        
        self.set_id_paquete(id_paquete)
        self.set_peso(peso)
        self.set_fragil(fragil)
        
        self.set_valor_kg(valor_kg)
        self.set_valor_envio(valor_envio)
        print("")

    def mostrar_venta(self):
        print("MOSTRAR VENTA")
        print(f"ID VENTA: {self.get_id_venta()}")
        print(f"FECHA: {self.get_fecha()}")

        print(f"NOMBRE: {self.get_nombre()}")
        print(f"APELLIDO: {self.get_apellido()}")
        print(f"IDENTIFICACIÓN: {self.get_identificacion()}")
        print(f"TELÉFONO: {self.get_telefono()}")
        print(f"EMAIL: {self.get_email()}")

        print(f"ID PAQUETE: {self.get_id_paquete()}")
        print(f"FRAGIL: {self.get_fragil()}")
        print(f"PESO PAQUETE (KG): {self.get_peso()}")

        print(f"VALOR KILO: ${self.get_valor_kg()}")
        print(f"VALOR ENVÍO: ${self.get_valor_envio()}")
        print("")

def main():
    print("VENTA 1")
    venta1 = Venta()
    venta1.crear_venta()
    venta1.mostrar_venta()

    print("VENTA 2")
    venta2 = Venta()
    venta2.crear_venta()
    venta2.mostrar_venta()
main()