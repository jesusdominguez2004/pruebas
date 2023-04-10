# Prueba grafo conexo VÉRTICES | Semana 9

def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    for siguiente in grafo[inicio] - visitados:
        dfs(grafo, siguiente, visitados)
    return visitados

def esConexo(grafo):
    inicio = next(iter(grafo))
    visitados = dfs(grafo, inicio)
    return len(visitados) == len(grafo), visitados

grafo_01 = {
    0:{1, 2}, 
    1:{0, 2}, 
    2:{0, 1}, 
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

print(f"Conexo grafo 01: {esConexo(grafo_01)}")
print(f"Conexo grafo 02: {esConexo(grafo_02)}")

