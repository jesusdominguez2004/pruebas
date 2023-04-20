# Prueba contar ciclos simples | Semana 10
class ListaAdyacencia:
    def __init__(self, grafo):
        self.grafo = grafo

    def contar_ciclos_desde_vertice(self, vertice):
        visitados = set() # conjunto para llevar registro de los vértices visitados
        ciclos = [] # lista para almacenar los ciclos encontrados

        # función auxiliar para recorrer el grafo en búsqueda de ciclos
        def encontrar_ciclos(desde, actual, ruta):
            visitados.add(actual)
            ruta.append(actual)

            for adyacente in self.grafo[actual]:
                if adyacente == desde and len(ruta) > 2:
                    ciclos.append(ruta[:])
                elif adyacente not in visitados:
                    encontrar_ciclos(desde, adyacente, ruta)

            ruta.pop()
            visitados.remove(actual)

        # buscar ciclos desde el vértice indicado
        encontrar_ciclos(vertice, vertice, [])

        # retornar el número de ciclos encontrados
        return len(ciclos)

grafo = {
    'A': ['B', 'C'],
    'B': ['C', 'D', 'E', 'A'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

grafo02 = {
    'A': ['B'],
    'B': ['C', 'E'],
    'C': ['D'],
    'D': ['A'],
    'E': ['D']
}

lista = ListaAdyacencia(grafo02)

vertices = ['A', 'B', 'C', 'D', 'E']
contador = 0
for i in vertices:
    ciclos = lista.contar_ciclos_desde_vertice(i)
    print(ciclos, type(ciclos)) # debería imprimir 1 en este caso
    contador = contador + ciclos

print("Caminos:", contador)
