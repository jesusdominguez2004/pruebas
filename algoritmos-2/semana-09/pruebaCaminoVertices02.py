# Prueba camino entre dos vértices | Semana 9 | Jesús Alberto Domínguez Charris

def camino_dfs_con_pila(self, inicio, fin):
    pila = [(inicio, [])]
    visitados = set()
    while pila:
        vertice, arcosVisitados = pila.pop()
        if vertice == fin:
            return arcosVisitados
        if vertice not in visitados:
            visitados.add(vertice)
            for arco in self.__listaVertices[vertice]:
                if arco.verticeFinal not in visitados:
                    pila.append((arco.verticeFinal, arcosVisitados + [arco]))
    return None

grafo = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
for inicial in vertices:
    for final in vertices:
        print(f"Existe camino entre {inicial} y {final}: {camino_dfs_con_pila(grafo, inicial, final)}")

