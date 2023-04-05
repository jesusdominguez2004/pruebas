from grafos_dijkstra2023 import GrafoLista
grafo01 = GrafoLista()
#Adicionar vértices
grafo01.adicionarVertice("D")
grafo01.adicionarVertice("C")
grafo01.adicionarVertice("B")
grafo01.adicionarVertice("H")
grafo01.adicionarVertice("R")
grafo01.adicionarVertice("A")
grafo01.adicionarVertice("T")
# #Adicionar arcos
grafo01.adicionarArco("D", "C")
grafo01.adicionarArco("D", "B")
grafo01.adicionarArco("C", "R")
grafo01.adicionarArco("R", "H")
grafo01.adicionarArco("H", "D")
grafo01.adicionarArco("H", "T")
grafo01.adicionarArco("H", "A")
grafo01.adicionarArco("B", "H")

print("El grafo es:\n",grafo01, sep="")
print("Recorrido DFS desde D:",grafo01.recorrerProfundidad("D"))
print("Recorrido DFS desde H:",grafo01.recorrerProfundidad("H"))
print("Recorrido BFS desde D:",grafo01.recorrerAnchura("D"))
