# Prueba 02 | Árboles binarios | Semana 14

from arbolesBinarios import *

# Creación de nodos árbol
nodoRaiz = NodosBinarios("A")
nodo01 = NodosBinarios("B")
nodo02 = NodosBinarios("C")
nodo03 = NodosBinarios("D")
nodo04 = NodosBinarios("E")
nodo05 = NodosBinarios("F")
nodo06 = NodosBinarios("G")
nodo07 = NodosBinarios("H")
nodo08 = NodosBinarios("I")

# Conexiones
nodoRaiz.setHijosNodo(nodo01, nodo02)
nodo01.setHijosNodo(nodo03, nodo04)
nodo02.setHijosNodo(nodo05, nodo06)
nodo03.setHijosNodo(nodo07, nodo08)

# 1. Hojas árbol
print(f"Ver hojas: {nodoRaiz.verHojasArbol()}")
print(f"Contar hojas: {nodoRaiz.contarHojasArbol()}\n")

# 2. Número de nodos
print(f"Ver nodos: {nodoRaiz.verNodosArbol()}")
print(f"Cantidad nodos: {nodoRaiz.contarNodosArbol()}\n")

# 3. Nodo padre
print(f"Ver padre de {nodo05}: {nodo05.verPadreNodo(nodoRaiz)}")

# 4. Profundidad nodo
print(f"Profundidad {nodo05}: {nodo05.profundidadNodo(nodoRaiz)}")

# 5. Altura árbol
print(f"Altura árbol: {nodo05.alturaArbol(nodoRaiz)}\n")

# 6. Nodos en nivel
print(f"Niveles árbol: {nodo05.contarNivelesArbol(nodoRaiz)}")
print(f"Ver nodos nivel 0: {nodoRaiz.verNodosNivel(0)}")
print(f"Ver nodos nivel 1: {nodoRaiz.verNodosNivel(1)}")
print(f"Ver nodos nivel 2: {nodoRaiz.verNodosNivel(2)}")
print(f"Ver nodos nivel 3: {nodoRaiz.verNodosNivel(3)}")
print(f"Contar nodos nivel 0: {nodoRaiz.contarNodosNivel(0)}")
print(f"Contar nodos nivel 1: {nodoRaiz.contarNodosNivel(1)}")
print(f"Contar nodos nivel 2: {nodoRaiz.contarNodosNivel(2)}")
print(f"Contar nodos nivel 3: {nodoRaiz.contarNodosNivel(3)}")
print(nodoRaiz.verArbol())

# 7. Árbol completo
print(f"¿Es árbol completo {nodoRaiz}?: {nodoRaiz.esArbolCompleto()}")
print(f"¿Es árbol completo {nodo01}?: {nodo01.esArbolCompleto()}")
print(f"¿Es árbol completo {nodo02}?: {nodo02.esArbolCompleto()}")
print(f"¿Es árbol completo {nodo03}?: {nodo03.esArbolCompleto()}")
print(f"¿Es árbol completo {nodo04}?: {nodo04.esArbolCompleto()}")
print(f"¿Es árbol completo {nodo05}?: {nodo05.esArbolCompleto()}")
print(f"¿Es árbol completo {nodo06}?: {nodo06.esArbolCompleto()}")
print(f"¿Es árbol completo {nodo07}?: {nodo07.esArbolCompleto()}")
print(f"¿Es árbol completo {nodo08}?: {nodo08.esArbolCompleto()}")

