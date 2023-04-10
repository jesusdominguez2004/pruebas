# Prueba camino entre dos vértices | Semana 9 | Jesús Alberto Domínguez Charris

def dfs(grafo, inicio, fin, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    if inicio == fin:
        return True
    for vecino in grafo[inicio] - visitados:
        if dfs(grafo, vecino, fin, visitados):
            return True
    return False

grafo = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
for inicial in vertices:
    for final in vertices:
        print(f"Existe camino entre {inicial} y {final}: {dfs(grafo, inicial, final)}")

