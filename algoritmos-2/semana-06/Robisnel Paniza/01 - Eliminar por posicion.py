# Eliminar en posición dada LISTA CIRCULAR SIMPLE

class NodoSimple:
    def __init__(self, valor) -> None:
        self.dato = valor
        self.siguiente = None


class ListaCircular:
    def __init__(self) -> None:
        self.raiz = None

    def insertarAlFinal(self, nodo_nuevo: NodoSimple) -> None:
        if self.raiz == None:
            self.raiz = nodo_nuevo
            self.raiz.siguiente = self.raiz
        else:
            nodoActual = self.raiz
            while nodoActual.siguiente != self.raiz:
                nodoActual = nodoActual.siguiente

            nodoActual.siguiente = nodo_nuevo
            nodo_nuevo.siguiente = self.raiz

    def imprimirIzquierdaDerecha(self) -> str:
        if self.raiz != None:
            recorrido = ''
            nodoActual = self.raiz
            while True:
                recorrido = recorrido + str(nodoActual.dato) + ' -> '
                nodoActual = nodoActual.siguiente
                if nodoActual == self.raiz:
                    recorrido = recorrido + str(self.raiz.dato)
                    return recorrido
                
    def cantidadNodos(self) -> int:
        if self.raiz == None:
            return 'Lista Circular Vacía'

        contador = 1
        nodoActual = self.raiz
        while nodoActual.siguiente != self.raiz:
            contador = contador + 1
            nodoActual = nodoActual.siguiente
        
        return contador
         
    def borrarEnPosicion(self, posicion: int):
        if self.raiz == None:
            return 'Lista Circualar Vacía'
        
        if posicion < 0:
            return 'Posición incorrecta...'

        if posicion >= self.cantidadNodos():
            return 'Posición incorrecta...'
        
        contador = 0
        nodoActual = self.raiz
        nodoPrevio = None
        while contador < posicion:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
            contador = contador + 1

        if nodoPrevio != None:
            nodoPrevio.siguiente = nodoActual.siguiente
        else:
            while nodoActual.siguiente != self.raiz:
                nodoActual = nodoActual.siguiente
            nodoActual.siguiente = self.raiz.siguiente
            self.raiz = self.raiz.siguiente
            
        return True


# Creación lista circular simple
lista = ListaCircular()
nodo1 = NodoSimple('A')
nodo2 = NodoSimple('B')
nodo3 = NodoSimple('C')
nodo4 = NodoSimple('D')

lista.insertarAlFinal(nodo1)
lista.insertarAlFinal(nodo2)
lista.insertarAlFinal(nodo3)
lista.insertarAlFinal(nodo4)

print(f'Lista circular simple: {lista.imprimirIzquierdaDerecha()}')
print(f'Cantidad nodos: {lista.cantidadNodos()}')

print(f'Eliminar en posición -1: {lista.borrarEnPosicion(-1)} ({lista.imprimirIzquierdaDerecha()})')
print(f'Eliminar en posición 0: {lista.borrarEnPosicion(0)} ({lista.imprimirIzquierdaDerecha()})')
print(f'Eliminar en posición 1: {lista.borrarEnPosicion(1)} ({lista.imprimirIzquierdaDerecha()})')
print(f'Eliminar en posición 2: {lista.borrarEnPosicion(2)} ({lista.imprimirIzquierdaDerecha()})')
