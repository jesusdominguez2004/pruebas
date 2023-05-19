# Prueba ver padre | Árboles binarios | Semana 14

from taller01 import *

# Creación de nodos árbol
nodoRaiz = NodosBinarios("A")
nodo01 = NodosBinarios("B")
nodo02 = NodosBinarios("C")
nodo03 = NodosBinarios("D")
nodo04 = NodosBinarios("E")
nodo05 = NodosBinarios("F")
nodo06 = NodosBinarios("C")

# Conexión forma 1
nodoRaiz.hijoIzquierdo = nodo01
nodoRaiz.hijoDerecho = nodo02

nodo02.hijoIzquierdo = nodo03

nodo03.hijoIzquierdo = nodo04
nodo03.hijoDerecho = nodo05
nodo04.hijoIzquierdo = nodo06

# Ver árbol forma 1
print(nodoRaiz.verArbol())

# Recorridos
print(f"Recorrido preorden: {nodoRaiz.preOrden()}")
print(f"Recorrido enorden: {nodoRaiz.enOrden()}")
print(f"Recorrido posorden: {nodoRaiz.preOrden()}")

# Hojas
print(f"{nodo01 = } es hoja: {nodo01.esHoja()}")
print(f"{nodo02 = } es hoja: {nodo02.esHoja()}")
print(f"{nodo03 = } es hoja: {nodo03.esHoja()}")
print(f"{nodo04 = } es hoja: {nodo04.esHoja()}")
print(f"{nodo05 = } es hoja: {nodo05.esHoja()}")
print(f"{nodo06 = } es hoja: {nodo06.esHoja()}")

# Hijos de un nodo
print(f"Ver hijos de {nodo02 = }: {nodo02.verHijosNodo()}")
print(f"Contar hijos de {nodo02 = }: {nodo02.contarHijosNodo()}")

nodo: NodosBinarios
for nodo in nodoRaiz.verNodosArbol():
    print(f"Padre de {nodo}: {nodo.verPadreNodo(nodoRaiz)}")
    