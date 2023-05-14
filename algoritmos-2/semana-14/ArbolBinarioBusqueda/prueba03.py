# Prueba 03 | ABB | Semana 14

from arbolBinarioBusqueda import *

# Árbol binario de búsqueda (ABB)
arbol01 = ArbolesBinariosBusqueda()
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

# Árbol binario (AB)
nodoRaiz = NodosBinarios(2)

# 2. Árbol parcialmente ordenado
listaElementos = [12, 20, 5, 73, 32, 12, 5, 17, 42, 32, 53]
arbolPO = nodoRaiz.arbolParcialmenteOrdenado(listaElementos)
print(f"AB parcialmente ordenado: \n{arbolPO.verArbol()}")

# 3. Dos árboles son iguales
arbolPO1 = nodoRaiz.arbolParcialmenteOrdenado([10, 30, 20, 15, 9, 7, 6])
arbolPO2 = nodoRaiz.arbolParcialmenteOrdenado([12, 20, 73, 32, 2, 7, 5])
calculo1 = OperadoraAB(arbolPO1, arbolPO2)
print(f"AB arbolPO1 y arbolPO2 son iguales: {calculo1.sonIguales()}")

arbol02 = ArbolesBinariosBusqueda()
arbol02.insertarNodo(40)
arbol02.insertarNodo(20)
arbol02.insertarNodo(60)
arbol02.insertarNodo(10)
arbol02.insertarNodo(30)
arbol02.insertarNodo(50)
arbol02.insertarNodo(70)
arbol02.insertarNodo(45)
arbol02.insertarNodo(55)
arbol02.insertarNodo(75)
calculo2 = OperadoraABB(arbol01, arbol02)
print(f"ABB arbol1 y arbol2 son iguales: {calculo2.sonIguales()}")

# 3. ABB con lista elementos
listaElementos = [10, 30, 20, 15, 9, 7, 6, 4, 3, 5]
arbol03 = ArbolesBinariosBusqueda()
arbol03.insertarNodosListaElementos(listaElementos)
print(f"ABB arbol03:\n{arbol03}")

# 4. ABB Es árbol AVL
print(f"ABB arbol01 AVL: {arbol01.esArbolAVL()} {arbol01.verFactoresEquilibrio()} {arbol01.contarFactoresEquilibrio()}")
print(f"ABB arbol02 AVL: {arbol02.esArbolAVL()} {arbol02.verFactoresEquilibrio()} {arbol02.contarFactoresEquilibrio()}")
print(f"ABB arbol03 AVL: {arbol03.esArbolAVL()} {arbol03.verFactoresEquilibrio()} {arbol03.contarFactoresEquilibrio()}\n")

# 5. ABB Es árbol degenerado
arbol04 = ArbolesBinariosBusqueda()
arbol04.insertarNodosListaElementos([40, 30, 20, 10, 0])
arbol05 = ArbolesBinariosBusqueda()
arbol05.insertarNodosListaElementos([40, 50, 60, 70, 80])
arbolPO3 = nodoRaiz.arbolParcialmenteOrdenado([40, 30, 20, 10, 0])
arbolPO4 = nodoRaiz.arbolParcialmenteOrdenado([40, 50, 60, 70, 80])

print(f"ABB arbol03 degenerado: {arbol03.esArbolDegenerado()}")
print(f"ABB arbol04 degenerado: {arbol04.esArbolDegenerado()}")
print(f"ABB arbol05 degenerado: {arbol05.esArbolDegenerado()}")
print(f"AB arbolPO1 degenerado: {arbolPO1.esArbolDegenerado()}")
print(f"AB arbolPO2 degenerado: {arbolPO2.esArbolDegenerado()}")
print(f"AB arbolPO3 degenerado: {arbolPO3.esArbolDegenerado()}")
print(f"AB arbolPO4 degenerado: {arbolPO4.esArbolDegenerado()}\n")

# 6. ABB Nodos aleatorios
arbol02.insertarNodosAleatorios(4) # Árbol existente
print(f"ABB arbol02:\n{arbol02}")

arbol06 = ArbolesBinariosBusqueda() # Árbol nuevo
arbol06.insertarNodosAleatorios(10)
print(f"ABB arbol06:\n{arbol06}")

# 7. ABB Lista fraccionarioss
listaFraccionarios = [1/2, 3/4, 1/6, 4/5, 3/2, 1/3, 7/4]
arbol07 = ArbolesBinariosBusqueda()
arbol07.insertarNodosListaFraccionarios(listaFraccionarios)
print(f"ABB arbol07:\n{arbol07}")
