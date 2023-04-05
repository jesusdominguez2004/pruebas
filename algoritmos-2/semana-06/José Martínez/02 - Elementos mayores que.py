# Eliminar elementos mayores que número ingresado

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.raiz = None
        self.cola = None

    def insertarFinal(self, nodoNuevo):
        if self.raiz == None:
            self.raiz = nodoNuevo
            self.cola = nodoNuevo
        else:
            actual = self.raiz
            while actual.siguiente != None:
                actual = actual.siguiente

            nodoNuevo.anterior = actual
            actual.siguiente = nodoNuevo
            self.cola = nodoNuevo

    def imprimirID(self) -> str:
        actual = self.raiz
        recorrido = ' None < - '
        while actual != None:
            recorrido = recorrido + str(actual.dato) + ' - '
            actual = actual.siguiente
        recorrido = recorrido + '> None'
        return recorrido
    
    def imprimirDI(self) -> str:
        actual = self.cola
        recorrido = ' None < - '
        while actual != None:
            recorrido = recorrido + str(actual.dato) + ' - '
            actual = actual.anterior
        recorrido = recorrido + '> None'
        return recorrido
    
    def insertarAlInicio(self, nodoNuevo):
        self.raiz.anterior = nodoNuevo
        nodoNuevo.siguiente = self.raiz
        self.raiz = nodoNuevo

    # MÉTODO RÚBRICA
    def eliminarMayoresQue(self, limite: int):
        if self.raiz == None:
            return None

        actual = self.raiz
        while actual is not None:
            if actual.dato > limite:
                siguiente_nodo = actual.siguiente
                if actual == self.raiz:
                    self.raiz = siguiente_nodo
                    if siguiente_nodo is not None:
                        siguiente_nodo.anterior = None
                elif actual == self.cola:
                    self.cola = actual.anterior
                    actual.anterior.siguiente = None
                else:
                    actual.anterior.siguiente = siguiente_nodo
                    siguiente_nodo.anterior = actual.anterior

                actual = siguiente_nodo
            else:
                actual = actual.siguiente


# Intanciar lista doble
lista = ListaDoble()

# Crear y añadir nodos dobles
nodo1 = NodoDoble(50)
nodo2 = NodoDoble(20)
nodo3 = NodoDoble(30)
nodo4 = NodoDoble(40)

lista.insertarFinal(nodo1)
lista.insertarFinal(nodo2)
lista.insertarFinal(nodo3)
lista.insertarFinal(nodo4)

# Imprimir lista normal e invertida
print(f'Lista doble normal: {lista.imprimirID()}')
print(f'Lista doble invertida: {lista.imprimirDI()}')

# Eliminar mayores que
lista.eliminarMayoresQue(40)
print(f'Lista doble normal: {lista.imprimirID()}')

lista.eliminarMayoresQue(30)
print(f'Lista doble normal: {lista.imprimirID()}')

lista.eliminarMayoresQue(20)
print(f'Lista doble normal: {lista.imprimirID()}')
