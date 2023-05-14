# Prueba 02 | ABB | Semana 14

from arbolBinarioBusqueda import *

# Árbol binario de búsqueda (ABB)
arbol01 = ArbolesBinariosBusqueda()
arbol01.insertarNodo(55)
arbol01.insertarNodo(30)
arbol01.insertarNodo(4)
arbol01.insertarNodo(41)
arbol01.insertarNodo(75)
arbol01.insertarNodo(85)
print(f"ABB:\n{arbol01}")

# Árbol binario (AB)
nodoRaiz = NodosBinarios("A")
nodo01 = NodosBinarios("B")
nodo02 = NodosBinarios("C")
nodo03 = NodosBinarios("D")
nodo04 = NodosBinarios("E")
nodo05 = NodosBinarios("F")
nodoRaiz.hijoIzquierdo = nodo01
nodoRaiz.hijoDerecho = nodo02
nodo02.hijoIzquierdo = nodo03
nodo03.hijoIzquierdo = nodo04
nodo03.hijoDerecho = nodo05
print(f"AB:\n{nodoRaiz.verArbol()}")

# 1. Ver nodo padre elemento
print(f"ABB Padre de 55: {arbol01.verPadreNodo(55)}")
print(f"ABB Padre de 4: {arbol01.verPadreNodo(4)}")
print(f"ABB Padre de 75: {arbol01.verPadreNodo(75)}")
print(f"ABB Padre de 41: {arbol01.verPadreNodo(41)}\n")

print(f"AB Padre de 'A': {nodoRaiz.verPadreNodo(nodoRaiz)}")
print(f"AB Padre de 'B': {nodo01.verPadreNodo(nodoRaiz)}")
print(f"AB Padre de 'C': {nodo02.verPadreNodo(nodoRaiz)}")
print(f"AB Padre de 'D': {nodo03.verPadreNodo(nodoRaiz)}")
print(f"AB Padre de 'E': {nodo04.verPadreNodo(nodoRaiz)}")
print(f"AB Padre de 'F': {nodo05.verPadreNodo(nodoRaiz)}\n")

# 2. Nodos a la máxima profundidad posible
print(f"Altura ABB: {arbol01.alturaArbol()}")
print(f"ABB Noda máxima profundiad: {arbol01.nodosEnMaximaProfundiad()}\n")

print(f"Altura AB: {nodoRaiz.alturaArbol(nodoRaiz)}")
print(f"AB Noda máxima profundiad: {nodoRaiz.nodosEnMaximaProfundiad(nodoRaiz)}\n")

# 3. Valor más cercano por encima de un dato indicado
print(f"ABB Ver nodos mayores que 40: {arbol01.verNodosMayoresQue(40)}")
print(f"ABB Contar nodos mayores que 40: {arbol01.contarNodosMayoresQue(40)}")
print(f"ABB Ver nodos menores que 40: {arbol01.verNodosMenoresQue(40)}")
print(f"ABB Contar nodos menores que 40: {arbol01.contarNodosMenoresQue(40)}")
print(f"ABB Mayor más cercano que 40: {arbol01.nodoMayorMasCercanoA(40)}")
print(f"ABB Menor más cercano que 40: {arbol01.nodoMenorMasCercanoA(40)}")

# 4. Menor y valor mayor en todo el árbol
print(f"ABB Nodo menor: {arbol01.menorNodo()}")
print(f"ABB Nodo mayor: {arbol01.mayorNodo()}")

# 5. Factor equilibrio árbol
print(f"ABB factor equilibrio: {arbol01.factorEquilibrio()}")
