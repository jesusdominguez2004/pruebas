# Prueba grafo conexo ARCOS | Semana 9

def dfs(grafo, inicio, arcosVisitados=None):
    if arcosVisitados is None:
        arcosVisitados = set()
    visitados = {inicio}
    cola = [inicio]
    while cola:
        vertice = cola.pop()
        for vecino in grafo[vertice]:
            if (vertice, vecino) not in arcosVisitados:
                visitados.add(vecino)
                arcosVisitados.add((vertice, vecino))
                cola.append(vecino)
    return visitados

def es_conexo(grafo):
    inicio = next(iter(grafo))
    arcosVisitados = set()
    visitados = dfs(grafo, inicio, arcosVisitados)
    return len(visitados) == len(grafo)

grafo_01 = {
    0:{1, 2}, 
    1:{0, 2}, 
    2:{0, 1, 3}, 
    3:{2}
}

grafo_02 = {
    "A": {"D"},
    "B": {"C"},
    "C": {"B", "D"},
    "D": {"A", "C"},
    "E": {"F"},
    "F": {"E"}
}   

print(f"Conexo grafo 01: {es_conexo(grafo_01)}")
print(f"Conexo grafo 02: {es_conexo(grafo_02)}")

