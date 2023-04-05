# Listas Circulares 2023

class NodoSimple:
    def __init__(self, valor) -> None:
        self.dato = valor
        self.siguiente = None


class ListaEnlazadaCircular:
    def __init__(self) -> None:
        self.raiz = None

    def insertarAlFinal(self, nodo_nuevo):
        if self.raiz != None:
            ultimo_nodo = self.raiz
            while ultimo_nodo.siguiente != self.raiz:
                ultimo_nodo = ultimo_nodo.siguiente

            ultimo_nodo.siguiente = nodo_nuevo
            nodo_nuevo.siguiente = self.raiz
        else:
            self.raiz = nodo_nuevo
            self.raiz.siguiente = self.raiz
    
    def imprimirIzquierdaDerecha(self):
        if self.raiz != None:
            nodo_temp = self.raiz
            while True:
                print(f" {nodo_temp.dato} ", end="->")
                nodo_temp = nodo_temp.siguiente
                if nodo_temp == self.raiz:
                    break
            print("")
    
    def imprimirDerechaIzquierda(self):
        if self.raiz is None:
            return

        # encontrar el último nodo en la lista
        nodo_final = self.raiz
        while nodo_final.siguiente != self.raiz:
            nodo_final = nodo_final.siguiente

        # recorrer la lista en sentido inverso
        nodo_actual = nodo_final
        while True:
            print(f" {nodo_actual.dato} ", end="<-")
            nodo_actual = self._obtenerNodoAnterior(nodo_actual)
            if nodo_actual == nodo_final:
                break
        print("")

    def _obtenerNodoAnterior(self, nodo):
        nodo_actual = self.raiz
        while nodo_actual.siguiente != nodo:
            nodo_actual = nodo_actual.siguiente
        return nodo_actual

    def eliminarPorPosicion(self, posicion):
        # Verificar que la lista no esté vacía
        if self.raiz is None:
            print("La lista está vacía")
            return

        # Si la posición a eliminar es la primera
        if posicion == 0:
            # Si la lista tiene varios nodos
            if self.raiz.siguiente != self.raiz:
                # Encontrar el último nodo
                ultimo_nodo = self.raiz
                while ultimo_nodo.siguiente != self.raiz:
                    ultimo_nodo = ultimo_nodo.siguiente

                # Actualizar el último nodo y la raíz
                ultimo_nodo.siguiente = self.raiz.siguiente
                self.raiz = self.raiz.siguiente
            # Si la lista tiene un solo nodo
            else:
                self.raiz = None
            return

        # Recorrer la lista hasta encontrar el nodo anterior al que se va a eliminar
        nodo_anterior = None
        nodo_actual = self.raiz
        for i in range(posicion):
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            # Si la posición a eliminar es mayor o igual al tamaño de la lista, no se puede eliminar ningún nodo
            if nodo_actual == self.raiz:
                print("La posición a eliminar es mayor o igual al tamaño de la lista")
                return

        # Actualizar el nodo anterior para que apunte al siguiente nodo del nodo que se va a eliminar
        nodo_anterior.siguiente = nodo_actual.siguiente


lista = ListaEnlazadaCircular()
nodo1 = NodoSimple("A")
nodo2 = NodoSimple("B")
nodo3 = NodoSimple("C")
lista.insertarAlFinal(nodo1)
lista.insertarAlFinal(nodo2)
lista.insertarAlFinal(nodo3)
lista.imprimirIzquierdaDerecha()
lista.imprimirDerechaIzquierda()

# Elminar nodo en posición dada
lista.eliminarPorPosicion(0)
lista.imprimirIzquierdaDerecha()
lista.eliminarPorPosicion(0)
lista.imprimirIzquierdaDerecha()