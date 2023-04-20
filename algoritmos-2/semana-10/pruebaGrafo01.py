# Prueba grafo 01 | Semana 10
from grafoCaminos import *

lista_01 = ListaAdyacencia()

lista_01.adicionarVertice("A")
lista_01.adicionarVertice("B")
lista_01.adicionarVertice("C")
lista_01.adicionarVertice("D")
lista_01.adicionarVertice("E")

lista_01.adicionarArco("A", "B", 2)
lista_01.adicionarArco("B", "C", 2)
lista_01.adicionarArco("B", "E", 2)
lista_01.adicionarArco("C", "D", 2)
lista_01.adicionarArco("D", "A", 2)
lista_01.adicionarArco("E", "D", 2)

print(f"Grafo 01: {lista_01}")
print(f"¿Hay ciclos?: {lista_01.alMenosUnCicloSimple()}")


for vertice in lista_01.verVertices():
    print(f"Ciclos de {vertice}: {lista_01.contarCiclosVertice(vertice)}")

print(f"Número de ciclos: {lista_01.contarCiclosSimples()}")
