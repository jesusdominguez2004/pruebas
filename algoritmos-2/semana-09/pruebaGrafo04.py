# Grafo caminos | Semana 9 | Jesús Alberto Domínguez Charris
from grafosCaminos import *

# 1. Instanciar lista de adyacencia
lista_01 = ListaAdyacencia()

# 2. Adicionar vértices
lista_01.adicionarVertice("A")
lista_01.adicionarVertice("B")
lista_01.adicionarVertice("C")
lista_01.adicionarVertice("F")

# 3. Adicionar arcos
lista_01.adicionarArco("A", "B", 2)
lista_01.adicionarArco("B", "A", 2)

lista_01.adicionarArco("B", "C", 2)
lista_01.adicionarArco("C", "B", 2)

print(f"Grafo 01: {lista_01}")
print(f"Lista Arcos: {lista_01.listaArcos()}")

# 4. Grafo no dirigido
print(f"¿El Grafo es no dirigido?: {lista_01.grafoNoDirigido()}")

# 5. Grafo dirigido
print(f"¿El Grafo es dirigido?: {lista_01.grafoDirigido()}")

# 6. Grafo conexo
print(f"¿El Grafo es conexo?: {lista_01.grafoConexo()}")
