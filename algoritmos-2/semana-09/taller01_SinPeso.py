"""
Taller 1 | Semana 9
- Obtener grado de salida de un nodo
- Obtener grado de entrada de un nodo
- Eliminar un arco existente en el grafo
- Eliminar un vértice existente en el grafo
- Indicar los nodos que tienen a otro como adyacente
- Implementar pesos en los arcos (Estructura de datos o una clase)
"""
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
        
    def adicionarArco(self, verticeInicial, verticeFinal):
        if self.existenAmbosVertices(verticeInicial, verticeFinal):
            buscarIninial = self.buscarVertice(verticeInicial)
            buscarIninial.add(verticeFinal)
    
    def buscarArco(self, verticeInicial, verticeFinal):
        if self.existenAmbosVertices(verticeInicial, verticeFinal):
            if verticeFinal in self.buscarVertice(verticeInicial):
                return True
                
    def verArcos(self):
        cadena = ""
        for vertice in self.__listaVertices:
            for elementoConjunto in self.__listaVertices[vertice]:
                cadena = cadena + f"{vertice} - {elementoConjunto}" + "%"
        cadena = cadena.split("%")
        if len(cadena) == 0:
            return []
        cadena.pop()
        return cadena

    def contarArcos(self):
        return len(self.verArcos())
    
    def verAdyacentesVertice(self, verticeBuscar):
        cadena = ""
        for elementoConjunto in self.__listaVertices[verticeBuscar]:
            cadena = cadena + str(elementoConjunto) + " "
        cadena = cadena.split()
        if len(cadena) == 0:
            return None
        return cadena
    
    def sonAdyacentes(self, verticeInicial, verticeFinal):
        if self.existenAmbosVertices(verticeInicial, verticeFinal):
            buscarIninial = self.buscarVertice(verticeInicial)
            return verticeFinal in buscarIninial
    
    def contarAdyacentesVertice(self, verticeBuscar):
        return len(self.__listaVertices.get(verticeBuscar))
    
    def contarAdyacentesTodos(self):
        cont = 0
        for vertice in self.__listaVertices:
            for _ in self.__listaVertices[vertice]:
                cont = cont + 1
        return cont
    
    def verAdyacentesTodos(self):
        cadena = ""
        for vertice in self.__listaVertices:
            for elementoConjunto in self.__listaVertices[vertice]:
                cadena = cadena + str(elementoConjunto) + " "
        cadena = cadena.split()
        if len(cadena) == 0:
            return {}
        cadena = set(cadena)
        return cadena
           
    def esConexionDirigida(self, vertice_1, vertice_2):
        if self.buscarArco(vertice_1, vertice_2) and self.buscarArco(vertice_2, vertice_1):
            return True
    
    def esConexionNoDirigida(self, vertice_1, vertice_2):
        if (self.buscarArco(vertice_1, vertice_2) or self.buscarArco(vertice_2, vertice_1)) and not self.esConexionDirigida(vertice_1, vertice_2):
            return True
        
    def __dfs(self, listaRecorrido: list, setVisitados: set, verticeActual):
        listaRecorrido.append(verticeActual)
        setVisitados.add(verticeActual)
        adyacentesActual = self.buscarVertice(verticeActual)
        for adyacente in adyacentesActual:
            if adyacente not in setVisitados:
                listaRecorrido, setVisitados = self.__bfs(listaRecorrido, setVisitados, adyacente)
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
            verticeCola = colaAdyacente.pop(0)
        adyacentesCola = self.buscarVertice(verticeCola)
        for adyacente in adyacentesCola:
            if adyacente not in setVisitados:
                listaRecorrido.append(adyacente)
                setVisitados.add(adyacente)
                colaAdyacente.append(adyacente)
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
        print(f"Ver adyacentes: {self.verAdyacentesTodos()}")
        print(f"Grafo dirigido: {self.grafoDirigido()}")
        print(f"Grafo no dirigido: {self.grafoNoDirigido()}\n")

    # 1. Obtener grado de salida de un nodo
    def gradoSalidaVertice(self, verticeBuscar):
        if self.buscarVertice(verticeBuscar) is None:
            return None
        cadena = ""
        for elementoConjunto in self.__listaVertices[verticeBuscar]:
            cadena = cadena + str(elementoConjunto) + " "
        cadena = cadena.split()
        return len(cadena)
    
    # 2. Obtener grado de entrada de un nodo
    def gradoEntradaVertice(self, verticeBuscar):
        if self.buscarVertice(verticeBuscar) is None:
            return None
        cont = 0
        for vertices in self.verVertices():
            if self.verAdyacentesVertice(vertices) is None:
                continue
            if verticeBuscar in self.verAdyacentesVertice(vertices):
                cont = cont + 1
        return cont
    
    # 3. Eliminar un arco existente en el grafo
    def eliminarArco(self, verticeInicial, verticeFinal):
        if not self.buscarArco(verticeInicial, verticeFinal):
            return None
        conjunto: set = self.__listaVertices[verticeInicial]
        conjunto.remove(verticeFinal)
        return True
        
    # 4. Eliminar un vértice existente en el grafo
    def eliminarVertice(self, verticeEliminar):
        for vertices in self.verVertices():
            self.eliminarArco(vertices, verticeEliminar)
        self.__listaVertices.pop(verticeEliminar)
        return True

    # 5. Indicar los nodos que tienen a otro como adyacente
    def verticesAdyacentes(self, verticeBuscar):
        if self.buscarVertice(verticeBuscar) is None:
            return "No existe"
        return self.verAdyacentesVertice(verticeBuscar)

    # 6. Implementar pesos en los arcos


# - - - - Prueba - - - - 

lista_01 = ListaAdyacencia()
lista_01.adicionarVertice("R")
lista_01.adicionarVertice("D")
lista_01.adicionarVertice("F")
lista_01.adicionarVertice("L")
lista_01.adicionarVertice("K")

lista_01.adicionarArco("R", "D")
lista_01.adicionarArco("D", "F")
lista_01.adicionarArco("D", "K")
lista_01.adicionarArco("F", "D")
lista_01.adicionarArco("F", "K")
lista_01.adicionarArco("L", "F")
lista_01.adicionarArco("L", "K")

print(f"Grafo 01: {lista_01}\n")

# 1. Grado de salida vértice
print(f"Grado salida 'R': {lista_01.gradoSalidaVertice('R')}")
print(f"Grado salida 'D': {lista_01.gradoSalidaVertice('D')}")
print(f"Grado salida 'F': {lista_01.gradoSalidaVertice('F')}")
print(f"Grado salida 'L': {lista_01.gradoSalidaVertice('L')}")
print(f"Grado salida 'K': {lista_01.gradoSalidaVertice('K')}\n")

# 2. Grado de entrada vértice
print(f"Grado entrada 'R': {lista_01.gradoEntradaVertice('R')}")
print(f"Grado entrada 'D': {lista_01.gradoEntradaVertice('D')}")
print(f"Grado entrada 'F': {lista_01.gradoEntradaVertice('F')}")
print(f"Grado entrada 'L': {lista_01.gradoEntradaVertice('L')}")
print(f"Grado entrada 'K': {lista_01.gradoEntradaVertice('K')}\n")

# 3. Eliminar un arco del grafo
print(f"Eliminar arco 'R - D': {lista_01.eliminarArco('R', 'D')}")
print(f"Arcos: {lista_01.verArcos()}\n")

# 4. Eliminar un vértice del grafo
print(f"Eliminar vértice 'K': {lista_01.eliminarVertice('K')}")
print(f"Vértices: {lista_01.verVertices()}")
print(f"Arcos: {lista_01.verArcos()}\n")

# 5. Vértices adyacentes de un vértice
print(f"Grafo 01: {lista_01}")
print(f"Vértices adyacentes de 'R': {lista_01.verticesAdyacentes('R')}")
print(f"Vértices adyacentes de 'D': {lista_01.verticesAdyacentes('D')}")
print(f"Vértices adyacentes de 'F': {lista_01.verticesAdyacentes('F')}")
print(f"Vértices adyacentes de 'L': {lista_01.verticesAdyacentes('L')}")
print(f"Vértices adyacentes de 'K': {lista_01.verticesAdyacentes('K')}")
