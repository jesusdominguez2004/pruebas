import json
class Ventas:
    def registro_clientes(self):
        clientes = {}
        i = 0
        while True:
            id       = input(f"Ingrese id cliente #{i}: ")
            nombre   = input(f"Ingrese nombre cliente #{i}: ").capitalize()
            correo   = input(f"Ingrese correo cliente #{i}: ")
            telefono = input(f"Ingrese telefono cliente #{i}: ")

            clientes[id] = {
                "ID": id,
                "NOMBRE": nombre,
                "CORREO": correo,
                "TELÉFONO": telefono
            }

            opc = input("¿Desea agregar a otro cliente? S/N: ").upper()
            if opc == "N": break
            i += 1

        with open("clientes.txt", "w") as archivo:
            json.dump(clientes, archivo)

    def registro_producto(self):
        productos = {}
        while True:
            referencia = input("Ingrese referencia producto: ")
            nombre     = input("Ingrese nombre producto: ").capitalize()
            precio     = input("Ingrese precio producto: ")

            productos[referencia] = {
                "NOMBRE": nombre,
                "REFERENCIA": referencia,
                "PRECIO": precio
            }

            opc = input("¿Desea agregar a otro producto? S/N: ").upper()
            if opc == "N": break

        with open("productos.txt", "w") as archivo:
            json.dump(productos, archivo)

    def registro_compra(self):
        compras = {}
        while True:
            with open("clientes.txt", "r") as archivo:
                clientes = json.load(archivo)
            id = input("Ingrese id cliente: ")

            if id in clientes:
                referencia = input("Ingrese la referencia del producto: ")
                with open("productos.txt","r") as archivo:
                    productos = json.load(archivo)

                if referencia in productos:
                    numero_factura = input("Ingrese número de la factira: ")
                    cantidad = input("Ingrese cantidad de producto de compra: ")
                    total = eval(productos[referencia]["PRECIO"]) * int(cantidad)
                    
                    compras[numero_factura] = {
                        "ID": clientes[id]["ID"],
                        "CLIENTE": clientes[id]["NOMBRE"],
                        "PRODUCTO": productos[referencia]["NOMBRE"],
                        "CANTIDAD": cantidad,
                        "TOTAL": total
                    } 
                    with open("compras.txt", "w") as archivo:
                        json.dump(compras, archivo)

                    print("DATOS COMPRA")
                    print(f"ID COMPRA : {numero_factura}")
                    print(f"CLIENTE   : {clientes[id]['NOMBRE']}")
                    print(f"NOMBRE    : {productos[referencia]['NOMBRE']}")
                    print(f"CANTIDAD  : {cantidad}")
                    print(f"PRECIO    : ${productos[referencia]['PRECIO']}")
                    print(f"TOTAL     : ${total}")

                    opc = input("¿Desea agregar a otra compra? S/N: ").upper()
                    if opc == "N": break

                else:
                    print(f"productos[{productos}] no existe...")
            else:
                print(f"clientes[{id}] no existe...")

    def listado_facturas(self):
        with open("compras.txt", "r") as archivo: 
            compras = json.load(archivo)
        contador = 1
        for i in compras:
            id       = compras[i]["ID"]
            cliente  = compras[i]["CLIENTE"]
            producto = compras[i]["PRODUCTO"]
            cantidad = compras[i]["CANTIDAD"]
            total    = compras[i]["TOTAL"]
            print(f"{contador}. ID: {id} | CLIENTE: {cliente} | PRODUCTO: {producto} | CANTIDAD: {cantidad} | TOTAL: ${total}")
            contador += 1
    
    def menu(self):
        while True:
            print("MENÚ\n1. REGISTRO CLIENTES\n2. REGISTRAR PRODUCTOS\n3. REGISTRAR COMPRA\n4. LISTA DE FACTURA\n5. SALIR")
            menu = input(">>> ")
            if menu == "1": self.registro_clientes()
            elif menu == "2": self.registro_producto()
            elif menu == "3": self.registro_compra()
            elif menu == "4": self.listado_facturas()
            elif menu == "5": return False
            else: print("Datos no válidos...")

def main():
    venta_1 = Ventas()
    venta_1.menu()

main()