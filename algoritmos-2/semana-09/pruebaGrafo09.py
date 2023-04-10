# Grafo caminos | Semana 9 | Jesús Alberto Domínguez Charris
from grafosCaminos import *

# 1. Instanciar lista de adyacencia
lista_01 = ListaAdyacencia()

# 2. Adicionar vértices
lista_01.adicionarVertice("A")
lista_01.adicionarVertice("B")
lista_01.adicionarVertice("C")
lista_01.adicionarVertice("D")
lista_01.adicionarVertice("E")
lista_01.adicionarVertice("F")

# 3. Adicionar arcos (CICLO PERO CAMINO SIMPLE)
lista_01.adicionarArco("A", "E")
lista_01.adicionarArco("B", "F")
lista_01.adicionarArco("C", "F")
lista_01.adicionarArco("F", "A")
lista_01.adicionarArco("E", "B")
lista_01.adicionarArco("E", "D")


print(f"Grafo 01: {lista_01}")
print(f"Lista Arcos: {lista_01.listaArcos()}")

# 4. Grafo no dirigido
print(f"¿El Grafo es no dirigido?: {lista_01.grafoNoDirigido()}")

# 5. Grafo dirigido
print(f"¿El Grafo es dirigido?: {lista_01.grafoDirigido()}")

# 6. Grafo conexo
print(f"¿El Grafo es conexo?: {lista_01.grafoConexo()}")

# 7. Grafo completo
print(f"¿El Grafo es completo?: {lista_01.grafoCompleto()}")

# 8. Camino entre vértices
vertices = lista_01.verVertices()
for inicial in vertices:
    for final in vertices:
        print(f"¿Hay un camino entre {inicial} y {final}?: {lista_01.caminoEntreDosVertices(inicial, final)}")

# 9. Al menos un ciclo
print(f"¿Grafo 01 tiene al menos un ciclo simples?: {lista_01.alMenosUnCicloSimple()}")

# 10. Contar ciclos simples
print(f"Ciclos simples: {lista_01.contarCiclosSimples()}")
