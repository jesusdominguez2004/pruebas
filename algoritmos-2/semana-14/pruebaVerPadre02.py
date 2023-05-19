# Prueba ver padre | Árboles binarios | Semana 14

from taller02 import *

arbol01 = ArbolesBinariosBusqueda() # ABB
arbol01.insertarNodo(40)
arbol01.insertarNodo(20)
arbol01.insertarNodo(60)
arbol01.insertarNodo(10)
arbol01.insertarNodo(30)
arbol01.insertarNodo(50)
arbol01.insertarNodo(70)
arbol01.insertarNodo(45)
arbol01.insertarNodo(55)
arbol01.insertarNodo(75)
print(f"ABB:\n{arbol01}")

# Llamar desde clase AB, Funciona
nodo: NodosBinarios
for nodo in arbol01.nodoRaiz.verNodosArbol():
    print(f"Padre de {nodo}: {nodo.verPadreNodo(arbol01.nodoRaiz)}")

print("")

# Llamar desde clase ABB, Funciona
nodo: NodosBinarios
for nodo in arbol01.nodoRaiz.verNodosArbol():
    print(f"Padre de {nodo}: {arbol01.verPadreNodo(nodo.valorNodo)}")
