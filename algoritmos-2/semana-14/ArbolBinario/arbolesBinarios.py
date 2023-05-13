# Árboles binarios | Semana 14 | Jesús Domínguez

"""
Colocar return en todo si es posibles, hasta las funciones privadas
Siempre complementar con una funcion privada especial, se puede reutilizar
Orar mucho

Ver altura (profundidad mayor) desde un nodo != nodoRaiz
ver nodos en nivel

Mutable (listas, no necesitan un return en las recursiones)
Inmutable (enteros, necesitan un return en las recursiones)

EMPEZAR ALGORITMOS EN SELF, Y NO COLOCAR ARGUMENTO NODORAIZ
ASÍ ES MÁS RECURSIVO, CADA NODO ES UN SUBÁRBOL

Árbol completo, mejorar con una función recursiva
"""

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

    # Métodos sobre los hijos
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
        
    # 1. Ver y contar hojas árbol
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

    # 2. Ver y contar nodos árbol
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

    # 3. Altura árbol
    def alturaArbol(self, nodoRaiz: "NodosBinarios"):
        listaNodos = nodoRaiz.verNodosArbol()
        mayor = 0
        nodo: NodosBinarios
        for nodo in listaNodos:
            profundidad = nodo.profundidadNodo(nodoRaiz)
            if profundidad > mayor: 
                mayor = profundidad
        return mayor

    # 4. Profundidad nodo
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
    
    # 5. Ver y contar nodos en nivel
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
    
    # 6. Árbol completo
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

    # Extra
    def esArbolCasiCompleto(self):
        return not self.esArbolCompleto()
    
    def verPadreNodo(self, nodoRaiz: "NodosBinarios"):
        if nodoRaiz is None or nodoRaiz == self:
            return None
        
        if nodoRaiz.hijoIzquierdo == self or nodoRaiz.hijoDerecho == self:
            return nodoRaiz
        
        hijoIzquierdo = self.verPadreNodo(nodoRaiz.hijoIzquierdo)
        hijoDerecho = self.verPadreNodo(nodoRaiz.hijoDerecho)
        return hijoIzquierdo or hijoDerecho
    