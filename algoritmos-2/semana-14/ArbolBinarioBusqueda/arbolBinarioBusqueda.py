# Árbol binario de búsqueda | Semana 14 | Jesús Domínguez

class NodosBinarios:
    def __init__(self, dato, nodoIzquierdo = None, nodoDerecho = None) -> None:
        self.valorNodo = dato
        self.hijoIzquierdo = nodoIzquierdo
        self.hijoDerecho = nodoDerecho
    
    def esHoja(self):
        return self.hijoIzquierdo is None and self.hijoDerecho is None
    
    def __str__(self) -> str:
        return str(self.valorNodo)

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, NodosBinarios):
            return False
        return self.valorNodo == otro.valorNodo
    
    # Métodos para ver árbol
    def verArbol(self) -> str:
        return self.__verArbolRecursivo(self, "")

    def __verArbolRecursivo(self, arbol: "NodosBinarios", recorrido: str, nivel = 0) -> str:
        if arbol is None:
            return ""
        espaciado = "\t" * nivel
        recorrido = espaciado + f"{arbol.valorNodo}\n" \
            + f"{self.__verArbolRecursivo(arbol.hijoIzquierdo, recorrido, nivel + 1)}" \
            + f"{self.__verArbolRecursivo(arbol.hijoDerecho, recorrido, nivel + 1)}" \
            + recorrido
        return recorrido
    
    # Recorridos
    def preOrden(self):
        visitados = list()
        self.__preOrdenRecursivo(self, visitados)
        return visitados
    
    def __preOrdenRecursivo(self, nodoActual: "NodosBinarios", visitados: list):
        if nodoActual is not None:
            visitados.append(nodoActual)
            visitados = self.__preOrdenRecursivo(nodoActual.hijoIzquierdo, visitados)
            visitados = self.__preOrdenRecursivo(nodoActual.hijoDerecho, visitados)
        return visitados
    
    def enOrden(self):
        visitados = list()
        self.__enOrdenRecursivo(self, visitados)
        return visitados
    
    def __enOrdenRecursivo(self, nodoActual: "NodosBinarios", visitados: list):
        if nodoActual is not None:
            visitados = self.__enOrdenRecursivo(nodoActual.hijoIzquierdo, visitados)
            visitados.append(nodoActual)
            visitados = self.__enOrdenRecursivo(nodoActual.hijoDerecho, visitados)
        return visitados
    
    def posOrden(self):
        visitados = list()
        self.__posOrdenRecursivo(self, visitados)
        return visitados
    
    def __posOrdenRecursivo(self, nodoActual: "NodosBinarios", visitados: list):
        if nodoActual is not None:
            visitados = self.__posOrdenRecursivo(nodoActual.hijoIzquierdo, visitados)
            visitados = self.__posOrdenRecursivo(nodoActual.hijoDerecho, visitados)
            visitados.append(nodoActual)
        return visitados

    # Métodos propios
    def verHijosNodo(self):
        return self.hijoIzquierdo, self.hijoDerecho
    
    def contarHijosNodo(self):
        cont = 0
        if self.hijoIzquierdo is not None:
            cont = cont + 1
        if self.hijoDerecho is not None:
            cont = cont + 1
        return cont
    
    def setHijosNodo(self, hijoIzquierdo: "NodosBinarios", hijoDerecho: "NodosBinarios"):
        self.hijoIzquierdo = hijoIzquierdo
        self.hijoDerecho = hijoDerecho

    def verPadreNodo(self, nodoRaiz: "NodosBinarios"):
        if nodoRaiz is None or nodoRaiz == self:
            return None
        
        if nodoRaiz.hijoIzquierdo == self or nodoRaiz.hijoDerecho == self:
            return nodoRaiz
        
        hijoIzquierdo = self.verPadreNodo(nodoRaiz.hijoIzquierdo)
        hijoDerecho = self.verPadreNodo(nodoRaiz.hijoDerecho)
        return hijoIzquierdo or hijoDerecho

    def verHojasArbol(self):
        listaHojas = []
        self.__hojasArbolRecursivo(self, listaHojas)
        return listaHojas
    
    def __hojasArbolRecursivo(self, nodo: "NodosBinarios",  listaHojas: list):
        if nodo is not None:
            if nodo.esHoja():
                listaHojas.append(nodo)
            self.__hojasArbolRecursivo(nodo.hijoIzquierdo, listaHojas)
            self.__hojasArbolRecursivo(nodo.hijoDerecho, listaHojas)
    
    def contarHojasArbol(self):
        return len(self.verHojasArbol())
    
    def verNodosArbol(self):
        listaNodos = []
        self.__nodosArbolRecursivo(self, listaNodos)
        return listaNodos

    def __nodosArbolRecursivo(self, nodo: "NodosBinarios",  listaNodos: list):
        if nodo is not None:
            listaNodos.append(nodo)
            self.__nodosArbolRecursivo(nodo.hijoIzquierdo, listaNodos)
            self.__nodosArbolRecursivo(nodo.hijoDerecho, listaNodos)
    
    def contarNodosArbol(self):
        return len(self.verNodosArbol())
    
    def alturaArbol(self, nodoRaiz: "NodosBinarios"):
        listaNodos = nodoRaiz.verNodosArbol()
        mayor = 0
        nodo: NodosBinarios
        for nodo in listaNodos:
            profundidad = nodo.profundidadNodo(nodoRaiz)
            if profundidad > mayor: 
                mayor = profundidad
        return mayor
    
    def profundidadNodo(self, nodoRaiz):
        numeroAncestros = 0
        numeroAncestros = self.__profundidadNodoRecursivo(self, nodoRaiz, numeroAncestros)
        return numeroAncestros
    
    def __profundidadNodoRecursivo(self, nodo: "NodosBinarios", nodoRaiz, numeroAncestros: int):
        if nodo is not None:
            padre = nodo.verPadreNodo(nodoRaiz)
            if padre is not None:
                numeroAncestros = numeroAncestros + 1
                return padre.__profundidadNodoRecursivo(padre, nodoRaiz, numeroAncestros)
        return numeroAncestros
    
    def verNodosNivel(self, nivel: int):
        listaNodos = []
        self.__verNodosNivelRecursivo(self, nivel, 0, listaNodos)
        return listaNodos
    
    def __verNodosNivelRecursivo(self, arbol: "NodosBinarios", nivelActual: int, nivelActualActual: int, listaNodos: list):
        if arbol is None:
            return
        if nivelActual == nivelActualActual:
            listaNodos.append(arbol)
        self.__verNodosNivelRecursivo(arbol.hijoIzquierdo, nivelActual, nivelActualActual + 1, listaNodos)
        self.__verNodosNivelRecursivo(arbol.hijoDerecho, nivelActual, nivelActualActual + 1, listaNodos)

    def contarNodosNivel(self, nivel: int):
        return len(self.verNodosNivel(nivel))

    def contarNivelesArbol(self, nodoRaiz): 
        return self.alturaArbol(nodoRaiz)
    
    def esArbolCompleto(self):
        nivelActual = 0
        nodosMaximos = 1
        while True:
            nodosNivel = self.contarNodosNivel(nivelActual)
            if nodosNivel == 0:
                break
            if nodosNivel != nodosMaximos:
                return False
            nivelActual = nivelActual + 1
            nodosMaximos = nodosMaximos * 2
        return True
    
    def esArbolCasiCompleto(self):
        return not self.esArbolCompleto()


class ArbolesBinariosBusqueda:
    def __init__(self) -> None:
        self.nodoRaiz = None

    def estaVacio(self) -> bool:
        return self.nodoRaiz == None
    
    def __str__(self) -> str:
        if not self.estaVacio():
            return self.nodoRaiz.verArbol()
        return ""
    
    def __repr__(self) -> str:
        return self.__str__()
    
    # Recorridos
    def preOrden(self):
        if not self.estaVacio():
            return self.nodoRaiz.preOrden()
        return None
    
    def enOrden(self):
        if not self.estaVacio():
            return self.nodoRaiz.enOrden()
        return None
    
    def posOrden(self):
        if not self.estaVacio():
            return self.nodoRaiz.posOrden()
        return None
    
    # Insertar
    def insertarNodo(self, elemento):
        if self.estaVacio():
            self.nodoRaiz = NodosBinarios(elemento)
        self.__insertarNodoRecursivo(self.nodoRaiz, elemento)
        
    def __insertarNodoRecursivo(self, arbol: NodosBinarios, elemento):
        if elemento == arbol.valorNodo:
            return
        if elemento < arbol.valorNodo:
            if arbol.hijoIzquierdo is None:
                arbol.hijoIzquierdo = NodosBinarios(elemento)
            else:
                self.__insertarNodoRecursivo(arbol.hijoIzquierdo, elemento)
        else:
            if arbol.hijoDerecho is None:
                arbol.hijoDerecho = NodosBinarios(elemento)
            else:
                self.__insertarNodoRecursivo(arbol.hijoDerecho, elemento)

    # Buscar
    def buscarNodo(self, elemento):
        if not self.estaVacio():
            return self.__buscarNodoRecursivo(self.nodoRaiz, elemento)
        return None
        
    def __buscarNodoRecursivo(self, arbol: NodosBinarios, elemento):
        if elemento == arbol.valorNodo:
            return arbol
        if elemento < arbol.valorNodo:
            if arbol.hijoIzquierdo is not None:
                return self.__buscarNodoRecursivo(arbol.hijoIzquierdo, elemento)
            else:
                return None
        else:
            if arbol.hijoDerecho is not None:
                return self.__buscarNodoRecursivo(arbol.hijoDerecho, elemento)
            else:
                return None

    # Eliminar
    def eliminarNodo(self, elemento):
        if not self.estaVacio():
            return self.__eliminarNodoRecursivo(self.nodoRaiz, elemento, None)
        return False

    def __eliminarNodoRecursivo(self, arbol: NodosBinarios, elemento, padre: NodosBinarios):
        if arbol is None:
            return False
        
        if elemento < arbol.valorNodo:
            return self.__eliminarNodoRecursivo(arbol.hijoIzquierdo, elemento, arbol)
        
        elif elemento > arbol.valorNodo:
            return self.__eliminarNodoRecursivo(arbol.hijoDerecho, elemento, arbol)
        
        else:
            # Nodo hoja (sin hijos)
            if arbol.esHoja():
                # Nodo hoja raíz
                if arbol == self.nodoRaiz:
                    self.nodoRaiz = None
                    return True
                # De lo contrario
                if padre.hijoIzquierdo == arbol:
                    padre.hijoIzquierdo = None
                else:
                    padre.hijoDerecho = None
                return True
            
            # Nodo con un hijo (derecho)
            if arbol.hijoIzquierdo is None and arbol.hijoDerecho is not None:
                # Nodo raíz
                if arbol == self.nodoRaiz:
                    self.nodoRaiz = arbol.hijoDerecho
                    return True
                # De lo contrario
                if padre.hijoIzquierdo is not None and padre.hijoIzquierdo == arbol:
                    padre.hijoIzquierdo = arbol.hijoDerecho
                else:
                    padre.hijoDerecho = arbol.hijoDerecho
                return True
            
            # Nodo con un hijo (izquierdo)
            if arbol.hijoIzquierdo is not None and arbol.hijoDerecho is None:
                # Nodo raíz
                if arbol == self.nodoRaiz:
                    self.nodoRaiz = arbol.hijoIzquierdo
                    return True
                # De lo contrario
                if padre.hijoIzquierdo is not None and padre.hijoIzquierdo == arbol:
                    padre.hijoIzquierdo = arbol.hijoIzquierdo
                else:
                    padre.hijoDerecho = arbol.hijoIzquierdo
                return True

            # Nodo con dos hijos (nodo interno)
            nodoIzquierdo: NodosBinarios = arbol.hijoIzquierdo
            nodoTemporal: NodosBinarios = None
            while nodoIzquierdo.hijoDerecho is not None:
                nodoTemporal = nodoIzquierdo
                nodoIzquierdo = nodoIzquierdo.hijoDerecho
            arbol.valorNodo = nodoIzquierdo.valorNodo

            if nodoTemporal is None:
                arbol.hijoIzquierdo = nodoIzquierdo.hijoIzquierdo
            elif nodoTemporal.hijoIzquierdo == nodoIzquierdo:
                nodoTemporal.hijoIzquierdo = nodoIzquierdo.hijoIzquierdo
            elif nodoTemporal.hijoDerecho == nodoIzquierdo:
                nodoTemporal.hijoDerecho = nodoIzquierdo.hijoIzquierdo
            return True