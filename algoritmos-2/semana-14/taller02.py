"""
Taller 02 | Árboles binarios | Semana 14

Para AB:
- Determinar el nodo padre para un elemento dado del árbol
- Determinar los elementos del árbol a la máxima profundidad posible

Para ABB:
- Determinar el valor más cercano por encima de un dato indicado.
- Determinar el menor y valor mayor en todo el árbol.
- Determinar el factor de equilibrio para el árbol
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

    def tieneUnHijo(self):
        if self.contarHijosNodo() == 1:
            return True
        
    def tieneDosHijos(self):
        if self.contarHijosNodo() == 2:
            return True

    def tieneHijos(self):
        if self.contarHijosNodo != 0:
            return True
    
    # 1. Determinar el nodo padre para un elemento dado del árbol
    def verPadreNodo(self, nodoRaiz: "NodosBinarios"):
        if nodoRaiz is None or nodoRaiz is self:
            return None      
        if (nodoRaiz.hijoIzquierdo is self or nodoRaiz.hijoDerecho is self) and nodoRaiz.valorNodo != self.valorNodo:
            return nodoRaiz  
        hijoIzquierdo = self.verPadreNodo(nodoRaiz.hijoIzquierdo)
        hijoDerecho = self.verPadreNodo(nodoRaiz.hijoDerecho)
        if hijoIzquierdo is not None:
            return hijoIzquierdo
        else:
            return hijoDerecho

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

    # 2. Determinar los elementos del árbol a la máxima profundidad posible
    def nodosEnMaximaProfundiad(self, nodoRaiz: "NodosBinarios"):
        alturaArbol = self.alturaArbol(nodoRaiz)
        nodosArbol = nodoRaiz.verNodosArbol()
        listaMaximos = []
        nodo: NodosBinarios
        for nodo in nodosArbol:
            if nodo.profundidadNodo(nodoRaiz) == alturaArbol:
                listaMaximos.append(nodo)
        return listaMaximos


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
    
    # 1. Determinar el nodo padre para un elemento dado del árbol
    def verPadreNodo(self, elemento):
        if not self.estaVacio():
            nodo = self.buscarNodo(elemento)
            if nodo is not None:
                return nodo.verPadreNodo(self.nodoRaiz)
        return None
    
    def alturaArbol(self):
        if not self.estaVacio():
            return self.nodoRaiz.alturaArbol(self.nodoRaiz)
        return None

    # 2. Determinar los elementos del árbol a la máxima profundidad posible
    def nodosEnMaximaProfundiad(self):
        if not self.estaVacio():
            alturaArbol = self.alturaArbol()
            nodosArbol = self.nodoRaiz.verNodosArbol()
            listaMaximos = []
            nodo: NodosBinarios
            for nodo in nodosArbol:
                if nodo.profundidadNodo(self.nodoRaiz) == alturaArbol:
                    listaMaximos.append(nodo)
            return listaMaximos
        return None
    
    # 3. Determinar el valor más cercano por encima de un dato indicado
    def verNodosMayoresQue(self, elemento):
        if not self.estaVacio():
            nodosMayores = []
            self.__verNodosMayoresQueRecursivo(self.nodoRaiz, elemento, nodosMayores)
            return nodosMayores
        return None

    def __verNodosMayoresQueRecursivo(self, arbol: NodosBinarios, elemento, nodosMayores: list):
        if arbol is None:
            return None
        if arbol.valorNodo > elemento:
            nodosMayores.append(arbol)
            self.__verNodosMayoresQueRecursivo(arbol.hijoIzquierdo, elemento, nodosMayores)
            self.__verNodosMayoresQueRecursivo(arbol.hijoDerecho, elemento, nodosMayores)
        else:
            self.__verNodosMayoresQueRecursivo(arbol.hijoDerecho, elemento, nodosMayores)

    def contarNodosMayoresQue(self, elemento):
        if not self.estaVacio():
            return len(self.verNodosMayoresQue(elemento))
        return None

    def nodoMayorMasCercanoA(self, elemento):
        if not self.estaVacio():
            if len(self.verNodosMayoresQue(elemento)) > 0:
                return min(self.verNodosMayoresQue(elemento), key=lambda nodoBinario: nodoBinario.valorNodo)
        return None
    
    def verNodosMenoresQue(self, elemento):
        if not self.estaVacio():
            nodosMenores = []
            self.__verNodosMenoresQueRecursivo(self.nodoRaiz, elemento, nodosMenores)
            return nodosMenores
        return None

    def __verNodosMenoresQueRecursivo(self, arbol: NodosBinarios, elemento, nodosMenores: list):
        if arbol is None:
            return None
        if arbol.valorNodo < elemento:
            nodosMenores.append(arbol)
            self.__verNodosMenoresQueRecursivo(arbol.hijoIzquierdo, elemento, nodosMenores)
            self.__verNodosMenoresQueRecursivo(arbol.hijoDerecho, elemento, nodosMenores)
        else:
            self.__verNodosMenoresQueRecursivo(arbol.hijoIzquierdo, elemento, nodosMenores)

    def contarNodosMenoresQue(self, elemento):
        if not self.estaVacio():
            return len(self.verNodosMenoresQue(elemento))
        return None
    
    def nodoMenorMasCercanoA(self, elemento):
        if not self.estaVacio():
            if len(self.verNodosMenoresQue(elemento)) > 0:
                return max(self.verNodosMenoresQue(elemento), key=lambda nodoBinario: nodoBinario.valorNodo)
        return None

    # 4. Determinar el menor y valor mayor en todo el árbol
    def menorNodo(self):
        if not self.estaVacio():
            menorNodo = self.nodoRaiz
            return self.__menorNodoRecursivo(self.nodoRaiz, menorNodo)
        return None

    def __menorNodoRecursivo(self, arbol: NodosBinarios, menorNodo: NodosBinarios):
        if arbol is None:
            return None
        if arbol.valorNodo < menorNodo.valorNodo:
            menorNodo = arbol
        menorNodoIzq: NodosBinarios = self.__menorNodoRecursivo(arbol.hijoIzquierdo, menorNodo)
        if menorNodoIzq is not None and menorNodoIzq.valorNodo < menorNodo.valorNodo:
            menorNodo = menorNodoIzq
        menorNodoDer: NodosBinarios = self.__menorNodoRecursivo(arbol.hijoDerecho, menorNodo)
        if menorNodoDer is not None and menorNodoDer.valorNodo < menorNodo.valorNodo:
            menorNodo = menorNodoDer
        return menorNodo

    def mayorNodo(self):
        if not self.estaVacio():
            mayorNodo = self.nodoRaiz
            return self.__mayorNodoRecursivo(self.nodoRaiz, mayorNodo)
        return None

    def __mayorNodoRecursivo(self, arbol: NodosBinarios, mayorNodo: NodosBinarios):
        if arbol is None:
            return mayorNodo
        if arbol.valorNodo > mayorNodo.valorNodo:
            mayorNodo = arbol
        mayorNodoIzq: NodosBinarios = self.__mayorNodoRecursivo(arbol.hijoIzquierdo, mayorNodo)
        mayorNodoDer: NodosBinarios = self.__mayorNodoRecursivo(arbol.hijoDerecho, mayorNodo)
        if mayorNodoIzq.valorNodo > mayorNodo.valorNodo:
            mayorNodo = mayorNodoIzq
        if mayorNodoDer.valorNodo > mayorNodo.valorNodo:
            mayorNodo = mayorNodoDer
        return mayorNodo

    # 5. Determinar el factor de equilibrio para el árbol
    def factorEquilibrio(self):
        if not self.estaVacio():
            if not self.nodoRaiz.esHoja():
                subArbolIzquierdo = self.nodoRaiz.hijoIzquierdo
                subArbolDerecho = self.nodoRaiz.hijoDerecho
                if subArbolIzquierdo is not None and subArbolDerecho is not None:
                    alturaIzquierda = subArbolIzquierdo.alturaArbol(subArbolIzquierdo)
                    alturaDerecha = subArbolDerecho.alturaArbol(subArbolDerecho)
                    return alturaIzquierda - alturaDerecha
        return None
    
# - - - - Prueba - - - -
arbol01 = ArbolesBinariosBusqueda() # ABB
arbol01.insertarNodo(40)
arbol01.insertarNodo(20)
arbol01.insertarNodo(60)
arbol01.insertarNodo(10)
arbol01.insertarNodo(30)
arbol01.insertarNodo(50)
arbol01.insertarNodo(70)
arbol01.insertarNodo(45)
arbol01.insertarNodo(55)
arbol01.insertarNodo(75)
print(f"ABB:\n{arbol01}")

nodoRaiz = NodosBinarios("A") # AB
nodo01 = NodosBinarios("B")
nodo02 = NodosBinarios("C")
nodo03 = NodosBinarios("D")
nodo04 = NodosBinarios("E")
nodo05 = NodosBinarios("F")
nodoRaiz.hijoIzquierdo = nodo01
nodoRaiz.hijoDerecho = nodo02
nodo02.hijoIzquierdo = nodo03
nodo03.hijoIzquierdo = nodo04
nodo03.hijoDerecho = nodo05
print(f"AB:\n{nodoRaiz.verArbol()}")

# 1. Determinar los nodos hoja de un árbol (AB y ABB)
print(f"ABB Padre de 55: {arbol01.verPadreNodo(55)}")
print(f"ABB Padre de 75: {arbol01.verPadreNodo(75)}")
print(f"ABB Padre de 23: {arbol01.verPadreNodo(23)}\n")

print(f"AB Padre de 'A': {nodoRaiz.verPadreNodo(nodoRaiz)}")
print(f"AB Padre de 'B': {nodo01.verPadreNodo(nodoRaiz)}")
print(f"AB Padre de 'C': {nodo02.verPadreNodo(nodoRaiz)}")
print(f"AB Padre de 'D': {nodo03.verPadreNodo(nodoRaiz)}")
print(f"AB Padre de 'E': {nodo04.verPadreNodo(nodoRaiz)}")
print(f"AB Padre de 'F': {nodo05.verPadreNodo(nodoRaiz)}\n")

# 2. Determinar el número de nodos de un árbol (AB y ABB)
print(f"Altura ABB: {arbol01.alturaArbol()}")
print(f"ABB Noda máxima profundiad: {arbol01.nodosEnMaximaProfundiad()}\n")

# 3. Valor más cercano por encima de un dato indicado (ABB)
print(f"ABB Ver nodos mayores que 40: {arbol01.verNodosMayoresQue(40)}")
print(f"ABB Mayor más cercano que 40: {arbol01.nodoMayorMasCercanoA(40)}")

# 4. Menor y valor mayor en todo el árbol (ABB)
print(f"ABB Nodo menor: {arbol01.menorNodo()}")
print(f"ABB Nodo mayor: {arbol01.mayorNodo()}")

# 5. Factor equilibrio árbol (ABB)
print(f"ABB factor equilibrio: {arbol01.factorEquilibrio()}")
