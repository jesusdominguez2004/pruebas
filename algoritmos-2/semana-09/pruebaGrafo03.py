# Grafo caminos | Semana 9 | Jesús Alberto Domínguez Charris
from grafosCaminos import *

# 1. Instanciar lista de adyacencia
lista_01 = ListaAdyacencia()

# 2. Adicionar vértices
lista_01.adicionarVertice("SFO")
lista_01.adicionarVertice("ORD")
lista_01.adicionarVertice("BOS")
lista_01.adicionarVertice("JFK")
lista_01.adicionarVertice("PVD")
lista_01.adicionarVertice("LAX")
lista_01.adicionarVertice("DFW")
lista_01.adicionarVertice("BWI")
lista_01.adicionarVertice("MIA")

# 3. Adicionar arcos
lista_01.adicionarArco("BOS", "SFO", 2704)
lista_01.adicionarArco("SFO", "BOS", 2704)
lista_01.adicionarArco("BOS", "ORD", 867)
lista_01.adicionarArco("ORD", "BOS", 867)
lista_01.adicionarArco("BOS", "JFK", 187)
lista_01.adicionarArco("JFK", "BOS", 187)
lista_01.adicionarArco("BOS", "MIA", 1258)
lista_01.adicionarArco("MIA", "BOS", 1258)
lista_01.adicionarArco("PVD", "JFK", 144)
lista_01.adicionarArco("JFK", "PVD", 144)
lista_01.adicionarArco("PVD", "ORD", 849)
lista_01.adicionarArco("ORD", "PVD", 849)
lista_01.adicionarArco("JFK", "ORD", 740)
lista_01.adicionarArco("ORD", "JFK", 740)
lista_01.adicionarArco("JFK", "BWI", 184)
lista_01.adicionarArco("BWI", "JFK", 184)
lista_01.adicionarArco("JFK", "MIA", 1090)
lista_01.adicionarArco("MIA", "JFK", 1090)
lista_01.adicionarArco("JFK", "DFW", 1391)
lista_01.adicionarArco("DFW", "JFK", 1391)
lista_01.adicionarArco("ORD", "SFO", 1846)
lista_01.adicionarArco("SFO", "ORD", 1846)
lista_01.adicionarArco("ORD", "DFW", 802)
lista_01.adicionarArco("DFW", "ORD", 802)
lista_01.adicionarArco("ORD", "BWI", 621)
lista_01.adicionarArco("BWI", "ORD", 621)
lista_01.adicionarArco("BWI", "MIA", 946)
lista_01.adicionarArco("MIA", "BWI", 946)
lista_01.adicionarArco("MIA", "DFW", 1121)
lista_01.adicionarArco("DFW", "MIA", 1121)
lista_01.adicionarArco("MIA", "LAX", 2342)
lista_01.adicionarArco("LAX", "MIA", 2342)
lista_01.adicionarArco("DFW", "SFO", 1464)
lista_01.adicionarArco("SFO", "DFW", 1464)
lista_01.adicionarArco("DFW", "LAX", 1235)
lista_01.adicionarArco("LAX", "DFW", 1235)
lista_01.adicionarArco("SFO", "LAX", 337)
lista_01.adicionarArco("LAX", "SFO", 337)
print(f"Grafo 01: {lista_01}\n")

# 4. Buscar vértices
print(f"Vértice 'SFO': {lista_01.buscarVertice('SFO')}")
print(f"Vértice 'ORD': {lista_01.buscarVertice('ORD')}")
print(f"Vértice 'BOS': {lista_01.buscarVertice('BOS')}")
print(f"Vértice 'JFK': {lista_01.buscarVertice('JFK')}")
print(f"Vértice 'PVD': {lista_01.buscarVertice('PVD')}")
print(f"Vértice 'LAX': {lista_01.buscarVertice('LAX')}")
print(f"Vértice 'DFW': {lista_01.buscarVertice('DFW')}")
print(f"Vértice 'BWI': {lista_01.buscarVertice('BWI')}")
print(f"Vértice 'MIA': {lista_01.buscarVertice('MIA')}\n")

# 5. Distancias mínimas Dijkstra
dijkstra_01 = Dijkstra(lista_01, "BWI")
dijkstra_01.inicializarDijikstra()
print(f"Camino hasta 'SFO': {dijkstra_01.obtenerCamino('SFO')}")
print(f"Camino hasta 'ORD': {dijkstra_01.obtenerCamino('ORD')}")
print(f"Camino hasta 'BOS': {dijkstra_01.obtenerCamino('BOS')}")
print(f"Camino hasta 'JFK': {dijkstra_01.obtenerCamino('JFK')}")
print(f"Camino hasta 'PVD': {dijkstra_01.obtenerCamino('PVD')}")
print(f"Camino hasta 'LAX': {dijkstra_01.obtenerCamino('LAX')}")
print(f"Camino hasta 'DFW': {dijkstra_01.obtenerCamino('DFW')}")
print(f"Camino hasta 'BWI': {dijkstra_01.obtenerCamino('BWI')}")
print(f"Camino hasta 'MIA': {dijkstra_01.obtenerCamino('MIA')}")
