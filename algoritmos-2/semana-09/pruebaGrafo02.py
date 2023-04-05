# Grafo con peso | Semana 9 | Jesús Alberto Domínguez Charris
from grafosConPesos import *

# 1. Instanciar lista de adyacencia
lista_01 = ListaAdyacencia()

# 2. Adicionar vértices
lista_01.adicionarVertice("A")
lista_01.adicionarVertice("B")
lista_01.adicionarVertice("C")
lista_01.adicionarVertice("D")

# 3. Adicionar arcos
lista_01.adicionarArco("A", "B", 2)
lista_01.adicionarArco("D", "C", 3)
lista_01.adicionarArco("A", "C", 3)
lista_01.adicionarArco("B", "D", 4)
print(f"Grafo 01: {lista_01}\n")

# 4. Buscar vértices
print(f"Buscar vertice 'A': {lista_01.buscarVertice('A')}")
print(f"Buscar vertice 'B': {lista_01.buscarVertice('B')}")
print(f"Buscar vertice 'C': {lista_01.buscarVertice('C')}")
print(f"Buscar vertice 'D': {lista_01.buscarVertice('D')}")
print(f"Buscar vertice 'E': {lista_01.buscarVertice('E')}\n")

# 5. Contar vértice
print(f"Contar vértice: {lista_01.contarVertices()}")

# 6. Existen ambos vértices
print(f"Existen 'A' y 'D': {lista_01.existenAmbosVertices('A', 'B')}")

# 7. Buscar arco con peso
print(f"Buscar arco 'A' a 'C' (peso 3): {lista_01.buscarArcoConPeso('A', 'C', 3)}")

# 8. Eliminar arco
print(f"Eliminar arco 'A' a 'C' (peso 3): {lista_01.eliminarArco('A', 'C', 3)}")
print(lista_01)

# 9. Eliminar vértice
print(f"Eliminar vértice 'B': {lista_01.eliminarVertice('B')}")
print(lista_01)

# 10. Ver arcos
print(f"Arcos: {lista_01.verArcos()}")

# 11. Contar arcos
print(f"Contar arcos: {lista_01.contarArcos()}")

# 12. Ver adyacentes vértice
print(f"Adyacentes de 'A': {lista_01.verAdyacentesVertice('A')}")
print(f"Adyacentes de 'B': {lista_01.verAdyacentesVertice('B')}")
print(f"Adyacentes de 'C': {lista_01.verAdyacentesVertice('C')}")
print(f"Adyacentes de 'D': {lista_01.verAdyacentesVertice('D')}")

# 13. Son adayacentes
lista_01.adicionarVertice("B")
lista_01.adicionarArco("C", "B", 5)
lista_01.adicionarArco("D", "B", 1)
lista_01.adicionarArco("C", "D", 3)
print(f"¿'B' es adyacente de 'A'?: {lista_01.sonAdyacentes('A', 'B')}")
print(f"¿'C' es adyacente de 'D'?: {lista_01.sonAdyacentes('D', 'C')}")
print(f"¿'B' es adyacente de 'C'?: {lista_01.sonAdyacentes('C', 'B')}")

# 14. Buscar arco sin peso
print(f"Buscar arco 'D' a 'C': {lista_01.buscarArcoSinPeso('D', 'C')}")

# 15. Contar adyacentes vértices
print(f"Contar adyacentes de 'A': {lista_01.contarAdyacentesVertice('A')}")
print(f"Contar adyacentes de 'B': {lista_01.contarAdyacentesVertice('B')}")
print(f"Contar adyacentes de 'C': {lista_01.contarAdyacentesVertice('C')}")
print(f"Contar adyacentes de 'D': {lista_01.contarAdyacentesVertice('D')}")

# 16. Contar adyacentes todos
print(f"Contar adyacentes grafo: {lista_01.contarAdyacentesTodos()}")

# 17. Ver adyacentes todos
print(f"Ver adyacentes grafo: {lista_01.verAdyacentesTodos()}")

# 18. Conexión dirigida vértices CON PESO
print(f"'D' a 'C': 3 son dirigidos (CON PESO): {lista_01.dirigidosConPeso('D', 'C', 3)}")
print(f"'D' a 'B': 1 son dirigidos (CON PESO): {lista_01.dirigidosConPeso('D', 'B', 1)}")

# 19. Conexión dirigida vértices SIN PESO
print(f"'D' a 'C' son dirigidos (SIN PESO): {lista_01.dirigidosSinPeso('D', 'C')}")
print(f"'D' a 'B' son dirigidos (SIN PESO): {lista_01.dirigidosSinPeso('D', 'B')}")

# 20. Conexión no dirigida vértices CON PESO
print(f"'D' a 'C': 3 NO son dirigidos (CON PESO): {lista_01.noDirigidosConPeso('D', 'C', 3)}")
print(f"'D' a 'B': 1 NO son dirigidos (CON PESO): {lista_01.noDirigidosConPeso('D', 'B', 1)}")

# 21. Conexión no dirigida vértices SIN PESO
print(f"'D' a 'C' NO son dirigidos (SIN PESO): {lista_01.noDirigidosSinPeso('D', 'C')}")
print(f"'D' a 'B' NO son dirigidos (SIN PESO): {lista_01.noDirigidosSinPeso('D', 'B')}\n")

# 22. Recorrido con profundidad DFS
print(f"Grafo 01: {lista_01}")
print(f"Recorrido DFS desde 'A': {lista_01.recorrerProfundidad('A')}")
print(f"Recorrido DFS desde 'B': {lista_01.recorrerProfundidad('B')}")
print(f"Recorrido DFS desde 'C': {lista_01.recorrerProfundidad('C')}")
print(f"Recorrido DFS desde 'D': {lista_01.recorrerProfundidad('D')}\n")

# 23. Recorrido con profundidad DFS
print(f"Grafo 01: {lista_01}")
print(f"Recorrido BFS desde 'A': {lista_01.recorrerAnchura('A')}")
print(f"Recorrido BFS desde 'B': {lista_01.recorrerAnchura('B')}")
print(f"Recorrido BFS desde 'C': {lista_01.recorrerAnchura('C')}")
print(f"Recorrido BFS desde 'D': {lista_01.recorrerAnchura('D')}\n")

# 24. Grado salida vértice
print(f"Grado salida de 'A': {lista_01.gradoSalidaVertice('A')}")
print(f"Grado salida de 'B': {lista_01.gradoSalidaVertice('B')}")
print(f"Grado salida de 'C': {lista_01.gradoSalidaVertice('C')}")
print(f"Grado salida de 'D': {lista_01.gradoSalidaVertice('D')}\n")

# 25. Grado entrada vértice
print(f"Grado entrada de 'A': {lista_01.gradoEntradaVertice('A')}")
print(f"Grado entrada de 'B': {lista_01.gradoEntradaVertice('B')}")
print(f"Grado entrada de 'C': {lista_01.gradoEntradaVertice('C')}")
print(f"Grado entrada de 'D': {lista_01.gradoEntradaVertice('D')}")
