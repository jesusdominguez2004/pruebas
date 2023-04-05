"""
Taller 1 | Semana 9 | Jesús Alberto Domínguez Charris

- Obtener grado de salida de un nodo
- Obtener grado de entrada de un nodo
- Eliminar un arco existente en el grafo
- Eliminar un vértice existente en el grafo
- Indicar los nodos que tienen a otro como adyacente
- Implementar pesos en los arcos (class Arco)
"""

# 6. Implementar pesos en los arcos (class Arco)
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
                
    def verArcos(self):
        cadena = ""
        for vertice in self.__listaVertices:
            for elementoConjunto in self.__listaVertices[vertice]:
                cadena = cadena + f"{elementoConjunto}" + "%"
        cadena = cadena.split("%")
        if len(cadena) == 0:
            return []
        cadena.pop()
        return cadena

    def contarArcos(self):
        return len(self.verArcos())

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

    def sonAdyacentes(self, verticeInicial, verticeFinal):
        if self.existenAmbosVertices(verticeInicial, verticeFinal):
            return self.buscarArcoSinPeso(verticeInicial, verticeFinal)
        
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

    def imprimirDatos(self):
        print(f"Lista: {self}")
        print(f"Contar vértices: {self.contarVertices()}")
        print(f"Ver vértices: {self.verVertices()}")
        print(f"Contar arcos: {self.contarArcos()}")
        print(f"Ver arcos: {self.verArcos()}")
        print(f"Contar adyacentes: {self.contarAdyacentesTodos()}")
        print(f"Ver adyacentes: {self.verAdyacentesTodos()}\n")

    # 1. Obtener grado de salida de un nodo
    def gradoSalidaVertice(self, verticeBuscar):
        if self.buscarVertice(verticeBuscar) is None:
            return None
        conjunto = self.buscarVertice(verticeBuscar)
        return len(conjunto)
    
    # 2. Obtener grado de entrada de un nodo
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
    
    # 3. Eliminar un arco existente en el grafo
    def eliminarArco(self, verticeInicial, verticeFinal, peso: int):
        if not self.buscarArcoConPeso(verticeInicial, verticeFinal, peso):
            return None
        arcoTemporal = Arco(verticeInicial, verticeFinal, peso)
        conjunto: set = self.__listaVertices[verticeInicial]
        conjunto.remove(arcoTemporal)
        return True
    
    # 4. Eliminar un vértice existente en el grafo
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
    
    # 5. Indicar los nodos que tienen a otro como adyacente
    def nodosAdyacentes(self, verticeBuscar):
        return self.verAdyacentesVertice(verticeBuscar)

# - - - - - Prueba - - - - -

lista01 = ListaAdyacencia()
lista01.adicionarVertice("A")
lista01.adicionarVertice("B")
lista01.adicionarVertice("C")
lista01.adicionarVertice("D")
lista01.adicionarArco("A", "C", 3)
lista01.adicionarArco("A", "D", 2)
lista01.adicionarArco("B", "A", 1)
lista01.adicionarArco("C", "D", 2)
lista01.adicionarArco("D", "A", 4)
lista01.adicionarArco("C", "B", 2)
lista01.adicionarArco("C", "A", 1)
print(f"Grafo 01: {lista01}")

# 1. Obtener grado de salida de un nodo
print(f"Grado de salida 'A': {lista01.gradoSalidaVertice('A')}")
print(f"Grado de salida 'B': {lista01.gradoSalidaVertice('B')}")
print(f"Grado de salida 'C': {lista01.gradoSalidaVertice('C')}")
print(f"Grado de salida 'D': {lista01.gradoSalidaVertice('D')}\n")

# 2. Obtener grado de entrada de un nodo
print(f"Grado de entrada 'A': {lista01.gradoEntradaVertice('A')}")
print(f"Grado de entrada 'B': {lista01.gradoEntradaVertice('B')}")
print(f"Grado de entrada 'C': {lista01.gradoEntradaVertice('C')}")
print(f"Grado de entrada 'D': {lista01.gradoEntradaVertice('D')}\n")

# 3. Eliminar un arco existente en el grafo
print(f"Eliminar arco '[D, A]: 4': {lista01.eliminarArco('D', 'A', 4)}")

# 4. Eliminar un vértice existente en el grafo
print(f"Eliminar vertice 'B': {lista01.eliminarVertice('B')}\n")

# 5. Indicar los nodos que tienen a otro como adyacente
print(f"Nodos adyacentes de 'A': {lista01.nodosAdyacentes('A')}")
print(f"Nodos adyacentes de 'B': {lista01.nodosAdyacentes('B')}")
print(f"Nodos adyacentes de 'C': {lista01.nodosAdyacentes('C')}")
print(f"Nodos adyacentes de 'D': {lista01.nodosAdyacentes('D')}\n")

# 6. Implementar pesos en los arcos (class Arco)
print(f"Arcos con pesos: {lista01.verArcos()}")
