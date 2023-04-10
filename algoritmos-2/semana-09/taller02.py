"""
Taller 2 | Semana 9 | Jesús Alberto Domínguez Charris

- Determinar si existe un camino válido entre dos vértices (línea 287)
- Determinar si el grafo tiene, al menos un ciclo (línea 320)
- Determinar si el grafo es fuertemente conexo (línea 344)
- Determinar si el grafo es completo (línea 360)
"""

import sys

class Arco:
    def __init__(self, verticeInical, verticeFinal, peso: int) -> None:
        self.verticeInicial = verticeInical
        self.verticeFinal = verticeFinal
        self.peso = peso

    def __repr__(self) -> str:
        return f"[{self.verticeInicial}, {self.verticeFinal}]: {self.peso}"

    def __str__(self) -> str:
        return self.__repr__()
    
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Arco):
            return False
        return self.verticeInicial == otro.verticeInicial and \
                self.verticeFinal == otro.verticeFinal and \
                self.peso == otro.peso
    
    def __hash__(self) -> int:
        return hash(str(self))


class ListaAdyacencia:
    def __init__(self) -> None:
        self.__listaVertices = dict()

    def __str__(self) -> str:
        return str(self.__listaVertices)
    
    def buscarVertice(self, datoBuscar):
        return self.__listaVertices.get(datoBuscar)

    def adicionarVertice(self, nuevoVertice):
        if self.buscarVertice(nuevoVertice) is None:
            listaAdyacentes = set()
            self.__listaVertices[nuevoVertice] = listaAdyacentes

    def verVertices(self):
        return list(self.__listaVertices.keys())

    def contarVertices(self):
        return len(self.__listaVertices)

    def existenAmbosVertices(self, verticeInicial, verticeFinal):
        buscarIninial = self.buscarVertice(verticeInicial)
        buscarFinal = self.buscarVertice(verticeFinal)
        if buscarIninial is None or buscarFinal is None:
            return False
        else:
            return True
    
    def adicionarArco(self, verticeInicial, verticeFinal, peso: int = 0):
        if self.existenAmbosVertices(verticeInicial, verticeFinal):
            arco = Arco(verticeInicial, verticeFinal, peso)
            buscarIninial: set = self.buscarVertice(verticeInicial)
            buscarIninial.add(arco)
    
    def buscarArcoConPeso(self, verticeInicial, verticeFinal, peso: int):
        if self.existenAmbosVertices(verticeInicial, verticeFinal):
            arcoTemporal = Arco(verticeInicial, verticeFinal, peso)
            return arcoTemporal in self.buscarVertice(verticeInicial)
    
    def buscarArcoSinPeso(self, verticeInicial, verticeFinal):
        if self.existenAmbosVertices(verticeInicial, verticeFinal):
            conjunto: set = self.buscarVertice(verticeInicial)
            arcos: Arco
            for arcos in conjunto:
                if verticeFinal == arcos.verticeFinal:
                    return True
            
    def eliminarArco(self, verticeInicial, verticeFinal, peso: int):
        if not self.buscarArcoConPeso(verticeInicial, verticeFinal, peso):
            return None
        arcoTemporal = Arco(verticeInicial, verticeFinal, peso)
        conjunto: set = self.__listaVertices[verticeInicial]
        conjunto.remove(arcoTemporal)
        return True
    
    def eliminarVertice(self, verticeEliminar):
        listaTemporal = []
        for vertices in self.verVertices():
            arco: Arco
            conjunto: set = self.__listaVertices[vertices]
            for arco in conjunto:
                if arco.verticeFinal == verticeEliminar:
                    listaTemporal.append(arco)
        arco: Arco
        for arco in listaTemporal:
            verticeInicial = arco.verticeInicial
            verticeFinal = arco.verticeFinal
            peso = arco.peso
            self.eliminarArco(verticeInicial, verticeFinal, peso)
        self.__listaVertices.pop(verticeEliminar)
        return True
                
    def listaArcos(self):
        listaArcos = []
        for vertices in self.verVertices():
            for arcos in self.buscarVertice(vertices):
                listaArcos.append(arcos)
        return listaArcos
    
    def contarArcos(self):
        return len(self.listaArcos())
    
    def sonAdyacentes(self, verticeInicial, verticeFinal):
        if self.existenAmbosVertices(verticeInicial, verticeFinal):
            return self.buscarArcoSinPeso(verticeInicial, verticeFinal)

    def verAdyacentesVertice(self, verticeBuscar):
        if self.buscarVertice(verticeBuscar) is None:
            return "No existe"
        return self.buscarVertice(verticeBuscar)
    
    def contarAdyacentesVertice(self, verticeBuscar):
        if self.buscarVertice(verticeBuscar) is None:
            return None
        return len(self.__listaVertices.get(verticeBuscar))
    
    def verAdyacentesTodos(self):
        cadena = ""
        for vertice in self.__listaVertices:
            for elementoConjunto in self.__listaVertices[vertice]:
                cadena = cadena + str(elementoConjunto) + "%"
        cadena = cadena.split("%")
        cadena.remove("")
        if len(cadena) == 0:
            return {}
        cadena = set(cadena)
        return cadena
    
    def contarAdyacentesTodos(self):
        cont = 0
        for vertice in self.__listaVertices:
            for _ in self.__listaVertices[vertice]:
                cont = cont + 1
        return cont
        
    def dirigidosConPeso(self, verticeInical, verticeFinal, peso: int):
        if self.buscarArcoConPeso(verticeInical, verticeFinal, peso) and self.buscarArcoConPeso(verticeFinal, verticeInical, peso):
            return True
    
    def dirigidosSinPeso(self, verticeInical, verticeFinal):
        if self.buscarArcoSinPeso(verticeInical, verticeFinal) and self.buscarArcoSinPeso(verticeFinal, verticeInical):
            return True
    
    def noDirigidosConPeso(self, verticeInical, verticeFinal, peso: int):
        if (self.buscarArcoConPeso(verticeInical, verticeFinal, peso) or self.buscarArcoConPeso(verticeFinal, verticeInical, peso)) and \
            not self.dirigidosConPeso(verticeInical, verticeFinal, peso):
            return True
    
    def noDirigidosSinPeso(self, verticeInical, verticeFinal):
        if (self.buscarArcoSinPeso(verticeInical, verticeFinal) or self.buscarArcoSinPeso(verticeFinal, verticeInical)) and \
            not self.dirigidosSinPeso(verticeInical, verticeFinal):
            return True
        
    def __dfs(self, listaRecorrido: list, setVisitados: set, verticeActual):
        listaRecorrido.append(verticeActual)
        setVisitados.add(verticeActual)
        arcoActual: Arco
        adyacentes = self.buscarVertice(verticeActual)
        for arcoActual in adyacentes:
            verticeFinal = arcoActual.verticeFinal
            if verticeFinal not in setVisitados:
                listaRecorrido, setVisitados = self.__dfs(listaRecorrido, setVisitados, verticeFinal)
        return listaRecorrido, setVisitados
    
    def recorrerProfundidad(self, verticeInicial):        
        if self.buscarVertice(verticeInicial) is None:
            return None        
        recorrido, visitados = self.__dfs(list(), set(), verticeInicial)
        for vertice in self.verVertices():
            if vertice not in visitados:
                recorrido, visitados = self.__dfs(recorrido, visitados, vertice)
        return recorrido
    
    def __bfs(self, listaRecorrido: list, setVisitados: set, verticeActual):
        listaRecorrido.append(verticeActual)
        setVisitados.add(verticeActual)
        colaAdyacente = [verticeActual]
        while colaAdyacente:
            arcoActual: Arco
            verticeCola = colaAdyacente.pop(0)        
            adyacentesActual = self.buscarVertice(verticeCola)
            for arcoActual in adyacentesActual:
                verticeFinal = arcoActual.verticeFinal
                if verticeFinal not in setVisitados:
                    listaRecorrido.append(verticeFinal)
                    setVisitados.add(verticeFinal)
                    colaAdyacente.append(verticeFinal)
        return listaRecorrido, setVisitados
    
    def recorrerAnchura(self, verticeInicial):
        if self.buscarVertice(verticeInicial) is None:
            return None        
        recorrido, visitados = self.__bfs(list(), set(), verticeInicial)
        for vertice in self.verVertices():
            if vertice not in visitados:
                recorrido, visitados = self.__bfs(recorrido, visitados, vertice)
        return recorrido

    def gradoSalidaVertice(self, verticeBuscar):
        if self.buscarVertice(verticeBuscar) is None:
            return None
        conjunto = self.buscarVertice(verticeBuscar)
        return len(conjunto)
    
    def gradoEntradaVertice(self, verticeBuscar):
        if self.buscarVertice(verticeBuscar) is None:
            return None
        cont = 0
        for vertices in self.verVertices():
            if self.verAdyacentesVertice(vertices) is None:
                continue
            arco: Arco
            for arco in self.verAdyacentesVertice(vertices):
                verticeFinal = arco.verticeFinal
                if verticeBuscar == verticeFinal:
                    cont = cont + 1
        return cont
    
    def imprimirDatos(self):
        print(f"Lista: {self}")
        print(f"Contar vértices: {self.contarVertices()}")
        print(f"Ver vértices: {self.verVertices()}")
        print(f"Contar arcos: {self.contarArcos()}")
        print(f"Ver arcos: {self.listaArcos()}")
        print(f"Contar adyacentes: {self.contarAdyacentesTodos()}")
        print(f"Ver adyacentes: {self.verAdyacentesTodos()}\n")
    
    def grafoDirigido(self):
        lista = []
        arco: Arco
        for arco in self.listaArcos():
            q = arco.verticeInicial
            w = arco.verticeFinal
            r = arco.peso
            arcoInvertido = Arco(w, q, r)
            if arcoInvertido not in self.listaArcos():
                return True
        return False

    def grafoNoDirigido(self):
        return not self.grafoDirigido()
    
    def __dfsConexo(self, inicio, arcosVisitados=None):
        if arcosVisitados is None:
            arcosVisitados = set()
        visitados = {inicio}
        stack = [inicio]
        while stack:
            vertice = stack.pop()
            vecino: Arco
            for vecino in self.__listaVertices[vertice]:
                if (vertice, vecino) not in arcosVisitados:
                    visitados.add(vecino.verticeFinal)
                    arcosVisitados.add((vertice, vecino))
                    stack.append(vecino.verticeFinal)
        return visitados

    def grafoConexo(self):
        lista = []
        arcosVisitados = set()
        for inicio in self.__listaVertices:
            visitadosInicio = self.__dfsConexo(inicio, arcosVisitados)
            lista.append(visitadosInicio)
            if len(visitadosInicio) == len(self.__listaVertices):
                arcosVisitados = set()
                continue
            else:
                return False
        return True
    
    # 1. Determinar si existe un camino válido entre dos vértices
    def caminoEntreDosVertices(self, inicio, fin):
        if self.existenAmbosVertices(inicio, fin) is None:
            return None
        pila = [(inicio, [])]
        visitados = set()
        while pila:
            vertice, arcosVisitados = pila.pop()
            if vertice == fin:
                return True
            if vertice not in visitados:
                visitados.add(vertice)
                arco: Arco
                for arco in self.__listaVertices[vertice]:
                    if arco.verticeFinal not in visitados:
                        pila.append((arco.verticeFinal, arcosVisitados + [arco]))
        return False
    
    # 2. Determinar si el grafo tiene, al menos un ciclo
    def __dfsUnCicloSimple(self, vertice, visitados:set, explorados=None, padre=None):
        if explorados is None:
            explorados = set()
        visitados.add(vertice)
        explorados.add(vertice)
        w: Arco 
        for w in self.__listaVertices[vertice]:
            if w.verticeFinal in explorados and w.verticeFinal != padre:
                return True
            elif w.verticeFinal not in visitados:
                if self.__dfsUnCicloSimple(w.verticeFinal, visitados, explorados, vertice):
                    return True
        explorados.remove(vertice)
        return False

    def alMenosUnCicloSimple(self):
        visitados = set()
        for vertice in self.__listaVertices:
            if vertice not in visitados:
                if self.__dfsUnCicloSimple(vertice, visitados):
                    return True
        return False
    
    # 3. Determinar si el grafo es fuertemente conexo
    def grafoFuertementeConexo(self):
        if not self.grafoDirigido():
            return False
        return self.grafoConexo()
    
    # 4. Determinar si el grafo es completo
    def grafoCompleto(self):
        if not self.grafoNoDirigido():
            return False
        for verticeInicial in self.verVertices():
            for verticeFinal in self.verVertices():
                if verticeInicial == verticeFinal:
                    continue
                if self.sonAdyacentes(verticeInicial, verticeFinal) or self.sonAdyacentes(verticeFinal, verticeInicial):
                    continue
                else:
                    return False
        return True


class Dijkstra:
    def __init__(self, grafo: ListaAdyacencia, verticeInical) -> None:
        self.__verticesUbicados = set()
        self.__verticesSinUbicar = set()
        self.__distancia = dict()
        self.__predecesores = dict()
        self.__verticeInicial = verticeInical
        self.__grafo = grafo

    def __calcularDistanciaMasCorta(self, vertice):
        distanciaVertice = self.__distancia.get(vertice)
        if distanciaVertice is None:
            return sys.maxsize
        else:
            return distanciaVertice
        
    def __buscarMinimo(self, vertices):
        verticeMinimo = None
        for verticeActual in vertices:
            if verticeMinimo is None:
                verticeMinimo = verticeActual
            else:
                if self.__calcularDistanciaMasCorta(verticeActual) < self.__calcularDistanciaMasCorta(verticeMinimo):
                    verticeMinimo = verticeActual
        return verticeMinimo
    
    def __buscarDistanciasMinimas(self, vertice):
        arco: Arco
        adyacentes = self.__grafo.buscarVertice(vertice)
        for arco in adyacentes:
            verticeAdyacente = arco.verticeFinal
            if self.__calcularDistanciaMasCorta(verticeAdyacente) > self.__calcularDistanciaMasCorta(vertice) + arco.peso:
                self.__distancia[verticeAdyacente] = self.__calcularDistanciaMasCorta(vertice) + arco.peso
                self.__predecesores[verticeAdyacente] = vertice
                self.__verticesSinUbicar.add(verticeAdyacente)
    
    def inicializarDijikstra(self):
        self.__distancia[self.__verticeInicial] = 0
        self.__verticesSinUbicar.add(self.__verticeInicial)
        while self.__verticesSinUbicar:
            mejorVertice = self.__buscarMinimo(self.__verticesSinUbicar)
            self.__verticesUbicados.add(mejorVertice)
            self.__verticesSinUbicar.remove(mejorVertice)
            self.__buscarDistanciasMinimas(mejorVertice)

    def obtenerCamino(self, verticeFinal):
        caminoEncontrado = []
        verticeActual = verticeFinal
        if self.__predecesores.get(verticeActual) is None:
            return None
        caminoEncontrado.append(verticeActual)
        while self.__predecesores.get(verticeActual):
            verticeActual = self.__predecesores[verticeActual]
            caminoEncontrado.append(verticeActual)
        caminoEncontrado.reverse()
        return caminoEncontrado

# - - - - - Prueba - - - - -

lista_01 = ListaAdyacencia() # Dirigido + no conexo
lista_01.adicionarVertice("A")
lista_01.adicionarVertice("B")
lista_01.adicionarVertice("C")
lista_01.adicionarVertice("D")
lista_01.adicionarArco("A", "B", 2)
lista_01.adicionarArco("B", "C", 3)
lista_01.adicionarArco("C", "D", 2)
lista_01.adicionarArco("D", "B", 1)

print(f"Grafo 01: {lista_01}")
print(f"¿Hay un camino de 'A' a 'D'?: {lista_01.caminoEntreDosVertices('A', 'D')}")
print(f"¿Hay al menos un ciclo simple?: {lista_01.alMenosUnCicloSimple()}")
print(f"¿Es fuertemente conexo?: {lista_01.grafoFuertementeConexo()}")
print(f"¿Es completo?: {lista_01.grafoCompleto()}\n")

lista_02 = ListaAdyacencia() # No dirigido + conexo
lista_02.adicionarVertice("A")
lista_02.adicionarVertice("B")
lista_02.adicionarVertice("C")
lista_02.adicionarVertice("D")
lista_02.adicionarArco("A", "B", 2)
lista_02.adicionarArco("B", "A", 2)
lista_02.adicionarArco("A", "C", 2)
lista_02.adicionarArco("C", "A", 2)
lista_02.adicionarArco("A", "D", 2)
lista_02.adicionarArco("D", "A", 2)
lista_02.adicionarArco("B", "C", 2)
lista_02.adicionarArco("C", "B", 2)
lista_02.adicionarArco("B", "D", 2)
lista_02.adicionarArco("D", "B", 2)
lista_02.adicionarArco("C", "D", 2)
lista_02.adicionarArco("D", "C", 2)

print(f"Grafo 02: {lista_02}")
print(f"¿Hay un camino de 'D' a 'B'?: {lista_02.caminoEntreDosVertices('D', 'B')}")
print(f"¿Hay al menos un ciclo simple?: {lista_02.alMenosUnCicloSimple()}")
print(f"¿Es fuertemente conexo?: {lista_02.grafoFuertementeConexo()}")
print(f"¿Es completo?: {lista_02.grafoCompleto()}\n")

lista_03 = ListaAdyacencia() # Dirigido + conexo
lista_03.adicionarVertice("A")
lista_03.adicionarVertice("B")
lista_03.adicionarVertice("C")
lista_03.adicionarVertice("D")
lista_03.adicionarVertice("E")

lista_03.adicionarArco("A", "B", 2)
lista_03.adicionarArco("B", "C", 3)
lista_03.adicionarArco("B", "E", 2)
lista_03.adicionarArco("C", "D", 4)
lista_03.adicionarArco("D", "A", 1)
lista_03.adicionarArco("E", "D", 3)

print(f"Grafo 03: {lista_03}")
print(f"¿Hay un camino de 'D' a 'E'?: {lista_03.caminoEntreDosVertices('D', 'E')}")
print(f"¿Hay al menos un ciclo simple?: {lista_03.alMenosUnCicloSimple()}")
print(f"¿Es fuertemente conexo?: {lista_03.grafoFuertementeConexo()}")
print(f"¿Es completo?: {lista_03.grafoCompleto()}")
