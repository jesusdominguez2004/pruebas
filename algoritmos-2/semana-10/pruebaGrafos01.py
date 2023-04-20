# Prueba grafos 1 | Semana 10
from grafoCaminos import *

lista_03 = ListaAdyacencia() # Dirigido + conexo
lista_03.adicionarVertice("A")
lista_03.adicionarVertice("B")
lista_03.adicionarVertice("C")
lista_03.adicionarVertice("D")
lista_03.adicionarVertice("E")

lista_03.adicionarArco("A", "B", 2)
lista_03.adicionarArco("B", "C", 3)
lista_03.adicionarArco("B", "E", 2)
lista_03.adicionarArco("C", "D", 4)
lista_03.adicionarArco("D", "A", 1)
lista_03.adicionarArco("E", "D", 3)

print(f"Grafo 03: {lista_03}")
print(f"¿Hay un camino de 'D' a 'E'?: {lista_03.caminoEntreDosVertices('D', 'E')}")
print(f"¿Hay al menos un ciclo simple?: {lista_03.alMenosUnCicloSimple()}")
print(f"¿Es fuertemente conexo?: {lista_03.grafoFuertementeConexo()}")
print(f"¿Es completo?: {lista_03.grafoCompleto()}\n")

print(f"Ciclos simples: {lista_03.contarCiclosSimples()}")

print(f"Paths A to B: {lista_03.verCaminosDosVertices('A', 'B')}")
print(f"Paths A to C: {lista_03.verCaminosDosVertices('A', 'C')}")
print(f"Paths A to D: {lista_03.verCaminosDosVertices('A', 'D')}")
print(f"Paths A to E: {lista_03.verCaminosDosVertices('A', 'E')}")


print(f"Cantidad Paths A to D: {lista_03.contarCaminosDosVertices('A', 'D')}")
print(f"Camino más largo A to D: {lista_03.caminoMasLargoDosVertice('A', 'D')}")
print(f"Camino más corto A to D: {lista_03.caminoMasCortoDosVertice('A', 'D')}")

