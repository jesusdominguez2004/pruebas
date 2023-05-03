# Árboles | Clase árboles | Semana 12

class Nodos:
    def __init__(self, x) -> None:
        self.dato = x
        self.izquierda = None
        self.derecha = None

    def __str__(self) -> str:
        return str(self.dato)
    

class Arboles:
    def __init__(self, x) -> None:
        self.nodoRaiz = Nodos(x)

    def __adicionarDatoRecursivamente(self, nodo: Nodos, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodos(dato)
            else:
                self.__adicionarDatoRecursivamente(nodo.izquierda, dato)
        
        else: # dato > nodo.dato
            if nodo.derecha is None:
                nodo.derecha = Nodos(dato)
            else:
                self.__adicionarDatoRecursivamente(nodo.derecha, dato)

    def adicionarDato(self, dato):
        self.__adicionarDatoRecursivamente(self.nodoRaiz, dato)
    


arbol01 = Arboles(0)
arbol01.adicionarDato(2)
arbol01.adicionarDato(1)
arbol01.adicionarDato(9)
arbol01.adicionarDato(3)
arbol01.adicionarDato(6)
arbol01.adicionarDato(5)
arbol01.adicionarDato(8)
arbol01.adicionarDato(7)


print("Nodo raíz:", arbol01.nodoRaiz)
print("Izquierda de 0:", arbol01.nodoRaiz.izquierda, "| Derecha de 0:", arbol01.nodoRaiz.derecha)
print("Izquierda de 2:", arbol01.nodoRaiz.derecha.izquierda, "| Derecha de 2:", arbol01.nodoRaiz.derecha.derecha)
print("Izquierda de 9:", arbol01.nodoRaiz.derecha.derecha.izquierda, "| Derecha de 9:", arbol01.nodoRaiz.derecha.derecha.derecha)
print("Izquierda de 3:", arbol01.nodoRaiz.derecha.derecha.izquierda.izquierda, "| Derecha de 3:", arbol01.nodoRaiz.derecha.derecha.izquierda.derecha)
print("Izquierda de 6:", arbol01.nodoRaiz.derecha.derecha.izquierda.derecha.izquierda, "| Derecha de 6:", arbol01.nodoRaiz.derecha.derecha.izquierda.derecha.derecha)
print("Izquierda de 5:", arbol01.nodoRaiz.derecha.derecha.izquierda.derecha.izquierda.izquierda, "| Derecha de 5:", arbol01.nodoRaiz.derecha.derecha.izquierda.derecha.izquierda.derecha)
print("Izquierda de 8:", arbol01.nodoRaiz.derecha.derecha.izquierda.derecha.derecha.izquierda, "| Derecha de 8:", arbol01.nodoRaiz.derecha.derecha.izquierda.derecha.derecha.derecha)
print("Izquierda de 7:", arbol01.nodoRaiz.derecha.derecha.izquierda.derecha.derecha.izquierda.izquierda, "| Derecha de 8:", arbol01.nodoRaiz.derecha.derecha.izquierda.derecha.derecha.izquierda.derecha)
