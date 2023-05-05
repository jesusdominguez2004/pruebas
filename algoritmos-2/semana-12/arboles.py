# Introducción a árboles | Semana 11

class Nodos:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.izquierda = None
        self.derecha = None


class Arboles:
    def __init__(self, dato) -> None:
        self.raiz = Nodos(dato)

    def __adicionarRecursivo(self, nodo: Nodos, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodos(dato)
            else:
                self.__adicionarRecursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodos(dato)
            else:
                self.__adicionarRecursivo(nodo.derecha, dato)

    def __inOrdenRecursivo(self, nodo: Nodos):
        if nodo is not None:
            self.__inOrdenRecursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inOrdenRecursivo(nodo.derecha)
            
    def __preOrdenRecursivo(self, nodo: Nodos):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preOrdenRecursivo(nodo.izquierda)
            self.__preOrdenRecursivo(nodo.derecha)

    def __postOrdenRecursivo(self, nodo: Nodos):
        if nodo is not None:
            self.__postOrdenRecursivo(nodo.izquierda)
            self.__postOrdenRecursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscarRecursivo(self, nodo: Nodos, busqueda):
        if nodo is None:
            return None
        
        if nodo.dato == busqueda:
            return nodo
        
        if busqueda < nodo.dato:
            return self.__buscarRecursivo(nodo.izquierda, busqueda)
        else:
            return self.__buscarRecursivo(nodo.derecha, busqueda)

    def adicionarDato(self, dato):
        self.__adicionarRecursivo(self.raiz, dato)

    def inOrden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inOrdenRecursivo(self.raiz)
        print("")

    def preOrden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preOrdenRecursivo(self.raiz)
        print("")

    def postOrden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postOrdenRecursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscarRecursivo(self.raiz, busqueda)
    
