# Prueba 01 | ABB | Semana 14

from arbolBinarioBusqueda import *

arbol01 = ArbolesBinariosBusqueda()
arbol01.insertarNodo(55)
arbol01.insertarNodo(30)
arbol01.insertarNodo(4)
arbol01.insertarNodo(41)
arbol01.insertarNodo(75)
arbol01.insertarNodo(85)

print(f"Árbol:\n{arbol01}")
print(f"Árbol vacío: {arbol01.estaVacio()}")
print(f"Pre Orden: {arbol01.preOrden()}")
print(f"En Orden: {arbol01.enOrden()}")
print(f"Pos Orden: {arbol01.posOrden()}")
print(f"Buscar 75: {arbol01.buscarNodo(75)}")
print(f"Buscar 15: {arbol01.buscarNodo(15)}")
print(f"Buscar 95: {arbol01.buscarNodo(95)}")

print(f"Eliminar 85 (hoja): {arbol01.eliminarNodo(85)}")
print(f"Eliminar 30 (dos hijos): {arbol01.eliminarNodo(30)}")

print(f"Árbol:\n{arbol01}")