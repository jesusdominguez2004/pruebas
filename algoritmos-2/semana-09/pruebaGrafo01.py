# Grafo sin peso | Semana 9 | Jesús Alberto Domínguez Charris
from grafosSinPesos import *

# 1. Instanciar lista de adyacencia
lista_01 = ListaAdyacencia()
lista_01.imprimirDatos()

# 2. Adicionar vértices
lista_01.adicionarVertice("A")
lista_01.adicionarVertice("B")
lista_01.adicionarVertice("C")
lista_01.adicionarVertice("D")
lista_01.imprimirDatos()

# 3. Adicionar arcos
lista_01.adicionarArco("A", "B")
lista_01.adicionarArco("A", "C")
lista_01.adicionarArco("A", "D")
lista_01.imprimirDatos()

# 4. Buscar vértices
print(f"Buscar vertice 'A': {lista_01.buscarVertice('A')}")
print(f"Buscar vertice 'B': {lista_01.buscarVertice('B')}")
print(f"Buscar vertice 'C': {lista_01.buscarVertice('C')}")
print(f"Buscar vertice 'D': {lista_01.buscarVertice('D')}")
print(f"Buscar vertice 'E': {lista_01.buscarVertice('E')}\n")

# 5. Dos vértices son adyacentes
print(f"¿A y B son adyacentes?: {lista_01.sonAdyacentes('A', 'B')}")
print(f"¿B y A son adyacentes?: {lista_01.sonAdyacentes('B', 'A')}\n")

# 6. Contar adyacentes de un vértice
print(f"Contar adyacentes de 'A': {lista_01.contarAdyacentesVertice('A')}")
print(f"Contar adyacentes de 'B': {lista_01.contarAdyacentesVertice('B')}")
print(f"Contar adyacentes de 'C': {lista_01.contarAdyacentesVertice('C')}")
print(f"Contar adyacentes de 'D': {lista_01.contarAdyacentesVertice('D')}\n")

# 7. Buscar arcos
print(f"¿Existe arco A y B?: {lista_01.buscarArco('A', 'B')}")
print(f"¿Existe arco B y A?: {lista_01.buscarArco('B', 'A')}\n")

# 8. Adicionar arcos
lista_01.adicionarArco("B", "A")
lista_01.adicionarArco("B", "C")
lista_01.adicionarArco("B", "D")
lista_01.imprimirDatos()

# 9. Tipo conexión entre dos vértices
print(f"¿A y B es dirigida?: {lista_01.esConexionDirigida('A', 'B')}")
print(f"¿B y A es dirigida?: {lista_01.esConexionDirigida('B', 'A')}")
print(f"¿A y B es no dirigida?: {lista_01.esConexionNoDirigida('A', 'B')}\n")

print(f"¿A y C es dirigida?: {lista_01.esConexionDirigida('A', 'C')}")
print(f"¿C y A es dirigida?: {lista_01.esConexionDirigida('C', 'A')}")
print(f"¿A y C es no dirigida?: {lista_01.esConexionNoDirigida('A', 'C')}\n")

# 10. Adyacentes de un vértice
print(f"Ver adyacentes de 'A': {lista_01.verAdyacentesVertice('A')}")
print(f"Ver adyacentes de 'B': {lista_01.verAdyacentesVertice('B')}")
print(f"Ver adyacentes de 'C': {lista_01.verAdyacentesVertice('C')}")
print(f"Ver adyacentes de 'D': {lista_01.verAdyacentesVertice('D')}\n")

# 11. Recorridos de profundidad DFS
print(f"Grafo: {lista_01}")
print(f"Recorrido DFS desde A: {lista_01.recorrerProfundidad('A')}")
print(f"Recorrido DFS desde B: {lista_01.recorrerProfundidad('B')}")
print(f"Recorrido DFS desde C: {lista_01.recorrerProfundidad('C')}")
print(f"Recorrido DFS desde D: {lista_01.recorrerProfundidad('D')}\n")

# 12. Recorridos de anchura BFS
print(f"Grafo: {lista_01}")
print(f"Recorrido BFS desde A: {lista_01.recorrerAnchura('A')}")
print(f"Recorrido BFS desde B: {lista_01.recorrerAnchura('B')}")
print(f"Recorrido BFS desde C: {lista_01.recorrerAnchura('C')}")
print(f"Recorrido BFS desde D: {lista_01.recorrerAnchura('D')}")
