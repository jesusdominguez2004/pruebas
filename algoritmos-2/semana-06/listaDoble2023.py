# Lista doble 2023

class NodoDoble:
    def __init__(self, valor):
        self.dato = valor
        self.anterior = None
        self.siguiente = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.nodoInical = None
        self.nodoFinal = None

    def insertarAlInicio(self, nodo_nuevo):
        if self.nodoInical is None:
            self.nodoInical = nodo_nuevo
            self.nodoFinal = nodo_nuevo
        else:
            nodo_nuevo.anterior = self.nodoFinal
            self.nodoFinal.siguiente = nodo_nuevo
            self.nodoFinal = nodo_nuevo

    def imprimirIzquierdaDerecha(self):
        current = self.nodoInical
        while current:
            print(current.dato, end=" <-> ")
            current = current.siguiente
        print()

    def imprimirDerechaIzquierda(self):
        current = self.nodoFinal
        while current:
            print(current.dato, end=" <-> ")
            current = current.anterior
        print()


lista = ListaEnlazadaDoble()
nodo1 = NodoDoble("A")
nodo2 = NodoDoble("B")
nodo3 = NodoDoble("C")
nodo4 = NodoDoble("D")
lista.insertarAlInicio(nodo1)
lista.insertarAlInicio(nodo2)
lista.insertarAlInicio(nodo3)
lista.insertarAlInicio(nodo4)
lista.imprimirIzquierdaDerecha()
lista.imprimirDerechaIzquierda()
