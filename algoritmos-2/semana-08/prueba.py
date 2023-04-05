# Prueba lista adyacente | Semana 8

# 1. Importar clase GrafoLista
from grafos2023 import GrafoLista

# 2. Crear grafo DIRIGIDO
grafo01 = GrafoLista()
print("Grafo:", grafo01)

# 3. Adicionar vértices (conjuntos)
grafo01.adicionarVertice("D")
grafo01.adicionarVertice("F")
grafo01.adicionarVertice("L")
grafo01.adicionarVertice("K")
grafo01.adicionarVertice("R")
print("Grafo:", grafo01)
print("Vértices (keys):", grafo01.verVertices())

# 4. Creación arcos
grafo01.adicionarArco("R", "D")
grafo01.adicionarArco("D", "F")
grafo01.adicionarArco("D", "K")
grafo01.adicionarArco("F", "D")
grafo01.adicionarArco("F", "K")
grafo01.adicionarArco("L", "F")
grafo01.adicionarArco("L", "K")
print("Grafo:", grafo01)

# - - - - RECORRIDOS - - - -

# DFS
grafo02 = GrafoLista()
grafo02.adicionarVertice("A")
grafo02.adicionarVertice("B")
grafo02.adicionarVertice("C")
grafo02.adicionarVertice("D")
grafo02.adicionarVertice("H")
grafo02.adicionarVertice("R")
grafo02.adicionarVertice("T")

grafo02.adicionarArco("B", "H")
grafo02.adicionarArco("C", "R")
grafo02.adicionarArco("D", "B")
grafo02.adicionarArco("D", "C")
grafo02.adicionarArco("H", "A")
grafo02.adicionarArco("H", "D")
grafo02.adicionarArco("H", "T")
grafo02.adicionarArco("R", "H")

print("\nGrafo 02:", grafo02)
print("Recorrido DFS desde A:", grafo02.recorrerProfundidad("A"))
print("Recorrido DFS desde B:", grafo02.recorrerProfundidad("B"))
print("Recorrido DFS desde D:", grafo02.recorrerProfundidad("D"))
print("Recorrido DFS desde C:", grafo02.recorrerProfundidad("C"))
print("Recorrido DFS desde H:", grafo02.recorrerProfundidad("H"))
print("Recorrido DFS desde R:", grafo02.recorrerProfundidad("R"))
print("Recorrido DFS desde T:", grafo02.recorrerProfundidad("T"))

# BFS
print("\nGrafo 02:", grafo02)
print("Recorrido BFS desde A:", grafo02.recorrerAnchura("A"))
print("Recorrido BFS desde B:", grafo02.recorrerAnchura("B"))
print("Recorrido BFS desde D:", grafo02.recorrerAnchura("D"))
print("Recorrido BFS desde C:", grafo02.recorrerAnchura("C"))
print("Recorrido BFS desde H:", grafo02.recorrerAnchura("H"))
print("Recorrido BFS desde R:", grafo02.recorrerAnchura("R"))
print("Recorrido BFS desde T:", grafo02.recorrerAnchura("T"))
