# Insertar al inicio LISTA DOBLE ENLAZADA

class NodoDoble:
    def __init__(self, valor) -> None:
        self.dato = valor
        self.siguiente = None
        self.anterior = None

    
class ListaDobleEnlazada:
    def __init__(self) -> None:
        self.raiz = None
        self.cola = None

    def insertarAlFinal(self, nodo_nuevo: NodoDoble) -> None:
        if self.raiz == None:
            self.raiz = nodo_nuevo
            self.cola = nodo_nuevo
        else:
            nodoActual = self.raiz
            while nodoActual.siguiente != None:
                nodoActual = nodoActual.siguiente

            nodo_nuevo.anterior = nodoActual
            nodoActual.siguiente = nodo_nuevo
            self.cola = nodo_nuevo
    
    def cantidadNodos(self) -> int:
        if self.raiz == None:
            return 'Lista Doble Enlazada Vacía'
        contador = 1
        nodoActual = self.raiz
        while nodoActual.siguiente != None:
            contador = contador + 1
            nodoActual = nodoActual.siguiente
        return contador

    def imprimirIzquierdaDerecha(self) -> str:
        nodoActual = self.raiz
        recorrido = ' None < - '
        while nodoActual != None:
            recorrido = recorrido + str(nodoActual.dato) + ' - '
            nodoActual = nodoActual.siguiente
        recorrido = recorrido + '> None'
        return recorrido
    
    def imprimirDerechaIzquierda(self) -> str:
        nodoActual = self.cola
        recorrido = ' None < - '
        while nodoActual != None:
            recorrido = recorrido + str(nodoActual.dato) + ' - '
            nodoActual = nodoActual.anterior
        recorrido = recorrido + '> None'
        return recorrido
    
    def insertarAlInicio(self, nodo_nuevo: NodoDoble) -> None:
        self.raiz.anterior = nodo_nuevo
        nodo_nuevo.siguiente = self.raiz
        self.raiz = nodo_nuevo


# Creación lista doble enlazada
lista = ListaDobleEnlazada()
nodo1 = NodoDoble('A')
nodo2 = NodoDoble('B')
nodo3 = NodoDoble('C')
nodo4 = NodoDoble('D')

lista.insertarAlFinal(nodo1)
lista.insertarAlFinal(nodo2)
lista.insertarAlFinal(nodo3)
lista.insertarAlFinal(nodo4)

print(f'Lista IZQUIERDA DERECHA: {lista.imprimirIzquierdaDerecha()}')
print(f'Lista DERECHA IZQUIERDA: {lista.imprimirDerechaIzquierda()}')
print(f'Cantidad nodos: {lista.cantidadNodos()}\n')

nodo5 = NodoDoble('Z')
lista.insertarAlInicio(nodo5)
print(f'Lista IZQUIERDA DERECHA: {lista.imprimirIzquierdaDerecha()}')
print(f'Lista DERECHA IZQUIERDA: {lista.imprimirDerechaIzquierda()}')
print(f'Cantidad nodos: {lista.cantidadNodos()}')
