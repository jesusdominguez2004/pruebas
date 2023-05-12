from arboles2023 import ArbolBinario
# Creacion de Nodos
# Cada nodo es un subárbol posible
raiz = ArbolBinario("A")
nodo01 = ArbolBinario("B")
nodo02 = ArbolBinario("C")
nodo03 = ArbolBinario("D")
nodo04 = ArbolBinario("E")
nodo05 = ArbolBinario("F")
nodo06 = ArbolBinario(25, ArbolBinario(40), ArbolBinario(50)) # Conexión nodos FORMA 1
# Conexion de nodos FORMA 2
raiz.hijo_izquierdo = nodo01
raiz.hijo_derecho = nodo02
nodo02.hijo_izquierdo = nodo03
nodo02.hijo_derecho = nodo04
nodo03.hijo_derecho = nodo05

# Una forma 3 puede ser métodos en class NodosBinarios...
# nodo03.setHijos(izquierdo, derecho)
# nodo03.setHijoIzquierdo(izquierdo)
# nodo03.setHijoDerecho(derecho)
# etc. 🤖⚙️🔧⛏️🔨⚒️

#Visualización CADA TAB ES UN NIVEL 
print("Arbol 1:\n",raiz.verArbol())

print("Árbol 2:\n", nodo06.verArbol())

# Con GRAFIS la visualización es mejor...
# Ver librería/módulo Grafis Python... 

print("Preorden arbol 1:", raiz.preOrden()) # Empieza en root y termina en root
print("Enorden arbol 1:", raiz.enOrden())
print("Posorden arbol 1:", raiz.posOrden())
