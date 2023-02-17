# Indicador | 3

#  Sistema de Ventas 
class Ventas:
    # Constructor
    def __init__(self):
        self.__codigo = [] # Creación de vector
        self.usuarios = []
        self.productos = []
        self.total_venta = []

    # SET: ------ almacenarCompras información
    def setCodigo(self, x:list):# codigo:list ---- especificar que tipo de valor tiene (codigos)
        self.__codigo = x # SET: Hay que pasarleun valor en este caso es la variable (codigo)

    # GET: ------ Delvolver información
    def getCodigo(self):
        return self.__codigo  # Se utiliza '__' antes de la variable para que la información sea privada
    
    def getCodigo(self):
        return self.__codigo  # Con el método GET retornamos la información sin importar que esta sea de manera privada :)

    def setUsuarios(self, x:list):
        self.usuarios = x

    def getUsuarios(self):
        return self.usuarios

    def setProducto(self, x:list):
        self.productos = x

    def getProductos(self):
        return self.productos

    def setTotalidad(self, x:list):
        self.total_venta = x

    def getTotalidad(self):
        return self.total_venta

# Llenar cada vector y mostrar sus datos:
    def almacenarCompras(self):
        cantidad = int(input('-> Escriba la cantidad de ventas: '))
        i = 0
        while i < cantidad:
            codigo = int(input(f'-> Escriba el código de venta[{i}]: '))
            usuario = input(f'-> Escriba usuario de venta[{i}]: ').capitalize() # La funcion de capitalize() se utiliza para que escriba las mayusculas de manera automatica en la consola
            producto = input(f'-> Escriba producto de venta[{i}] (computador = 1 / tablet = 2 / celular = 3): ').capitalize()

            # Método de guardado: para que el vector obtenga un valor asignado y guarde la ubicacion de este
            self.getCodigo().append(codigo)
            self.getUsuarios().append(usuario)
            if producto == 'Computador' or producto == '1': 
                self.getProductos().append('Computador')
                self.getTotalidad().append(500000)
            elif producto == 'Tablet' or producto == '2': 
                self.getProductos().append('Tablet')
                self.getTotalidad().append(200000)
            elif producto == 'Celular' or producto == '3': 
                self.getProductos().append('Celular')
                self.getTotalidad().append(100000)
            else:
                print('Producto incorrecto')
                self.getProductos().append('Ninguno')
                self.getTotalidad().append(0)
            i = i + 1
            print('')

# Mostrar información por medio de GET
    def imprimirCompras(self):
        # print(f'Vector: {self.get_vector()}') -- SE IMPRIME EL VECTOR EN UNA SOLA LÍNEA --
        print('<- Imprimir compras')
        print(f'<- Codigos compra: {self.getCodigo()}')
        print(f'<- Usuarios compra: {self.getUsuarios()}')
        print(f'<- Productos compra: {self.getProductos()}')
        print(f'<- Totales compra: {self.getTotalidad()}')

    # Métodos de almacenamiento en txt
    def codigoDelProducto(self):
        print('')
        print('<- Código del producto')
        codigo = int(input('-> Escriba código a buscar: '))

        if codigo in self.getCodigo(): # si existe
            i = 0
            while i < len(self.getCodigo()):
                if codigo == self.getCodigo()[i]:
                    print(f'<- {self.getProductos()[i]}')
                    archivo = open('codigoDelProducto.txt', 'w')
                    archivo.write(f'{self.getProductos()[i]}')
                    archivo.close()
                    break
                i = i + 1
        else: # si no
            print(f'{codigo} no existe en compras :(')

    def comprasDelUsuario(self):
        print('')
        print('<- Compras del usuario')
        usuario = input('-> Escriba usuario a buscar: ').capitalize()
        if usuario in self.getUsuarios(): # si existe
            archivo = open('comprar_usuarios.txt', 'w')
            i = 0
            cont = 1
            while i < len(self.getUsuarios()):
                if usuario == self.getUsuarios()[i]:
                    print(f'<- {cont}. {self.getProductos()[i]} (${self.getTotalidad()[i]})')
                    archivo.write(f'{cont}. {self.getProductos()[i]} (${self.getTotalidad()[i]})' + '\n')
                    cont = cont + 1
                i = i + 1
            archivo.close()
        else: # si no      
            print(f'{usuario} no existe en compras :(')

    def promedioCompras(self):
        print('')
        print('<- Promedio compras')
        suma = 0
        i = 0
        while i < len(self.getTotalidad()):
            suma = suma + self.getTotalidad()[i]
            i = i + 1
        num_compras = len(self.getTotalidad())
        promedio = suma / num_compras
        promedio = round(promedio, 2)
        print(f'<- ${promedio}')
        archivo = open('promedioCompras.txt', 'w')
        archivo.write(f'${promedio}')
        archivo.close()

    def masVendido(self):
        print('')
        print('<- Producto más vendido')

        # cuandos computadores, tablets y celulares hay -----
        cont_computadores = 0
        cont_tablets = 0
        cont_celulares = 0
        i = 0
        while i < len(self.getProductos()):
            if self.getProductos()[i] == 'Computador':
                cont_computadores = cont_computadores + 1

            if self.getProductos()[i] == 'Tablet':
                cont_tablets = cont_tablets + 1

            if self.getProductos()[i] == 'Celular':
                cont_celulares = cont_celulares + 1
            i = i + 1

        cuantos_hay = []
        cuantos_hay.append(cont_computadores)
        cuantos_hay.append(cont_tablets)
        cuantos_hay.append(cont_celulares)

        # mostrar en consola cuantos hay -----
        print(f'<- 1. Hay {cuantos_hay[0]} computadores comprados')
        print(f'<- 2. Hay {cuantos_hay[1]} tablets comprados')
        print(f'<- 3. Hay {cuantos_hay[2]} celulares comprados')

        # el número mayor en cuantos_hay es el más vendido -----
        productos = ['Computador', 'Tablet', 'Celular']
        mas_vendido = cuantos_hay[0]
        su_nombre_es = productos[0]
        i = 0
        while i < len(cuantos_hay):
            if cuantos_hay[i] > mas_vendido:
                mas_vendido = cuantos_hay[i]
                su_nombre_es = productos[i]
            i = i + 1 

        # preguntar cuántas veces aparece el número de más vendido -----
        cont = 0
        i = 0
        while i < len(cuantos_hay):
            if cuantos_hay[i] == mas_vendido: 
                cont = cont + 1
            i = i + 1

        # resultado cuando solo hay un producto mas vendido -----
        if cont == 1:
            print(f'<- {su_nombre_es} es el mas vendido')
            # guardar en txt
            archivo = open('masVendido.txt', 'w')
            archivo.write(f'{su_nombre_es} es el mas vendido')
            archivo.close()

        # resultado cuando NO solo hay un producto mas vendido -----
        if cont != 1:
            # guardar en txt de esta forma + imprimir consola resultados
            archivo = open('masVendido.txt', 'w')
            i = 0
            while i < len(cuantos_hay):
                if cuantos_hay[i] == mas_vendido:
                    print(f'<- {productos[i]}')                    
                    archivo.write(f'{productos[i]}' + '\n')
                i = i + 1
            archivo.close()

    def usuariosDelProducto(self):
        print('')
        print('<- Usuarios del producto')
        producto = input('-> Escriba producto a buscar (computador = 1 / tablet = 2 / celular = 3): ').capitalize()

        if producto == 'Computador' or producto == '1': 
            producto = 'Computador'
        elif producto == 'Tablet' or producto == '2': 
            producto == 'Tablet'
        elif producto == 'Celular' or producto == '3': 
            producto == 'Celular'
        else:
            producto = 'Ninguno'

        if producto in self.getProductos(): # si existe
            # guardar en txt de esta forma + imprimir consola resultados 
            archivo = open('usuarios_productos.txt', 'w')
            i = 0
            cont = 1
            while i < len(self.getProductos()):
                if self.getProductos()[i] == producto:
                    print(f'<- {self.getUsuarios()[i]}')
                    archivo.write(f'{self.getUsuarios()[i]}' + '\n')
                    cont = cont + 1
                i = i + 1
            archivo.close()
        else: # si no
            print(f'{producto} no existe en compras :(')

def main():
    made = Ventas()
    made.almacenarCompras()
    made.imprimirCompras()
    made.codigoDelProducto()
    made.comprasDelUsuario()
    made.promedioCompras()
    made.masVendido()
    made.usuariosDelProducto()
main()
# Se llama la función 