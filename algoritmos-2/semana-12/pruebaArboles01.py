# Introducción a árboles | Semana 11

from arboles import *

# 0 1 2 3 7 8 9 4 5 6
arbol_01 = Arboles(0)
arbol_01.adicionarDato(1)
arbol_01.adicionarDato(2)
arbol_01.adicionarDato(3)
arbol_01.adicionarDato(7)
arbol_01.adicionarDato(8)
arbol_01.adicionarDato(9)
arbol_01.adicionarDato(4)
arbol_01.adicionarDato(5)
arbol_01.adicionarDato(6)
arbol_01.inOrden()
arbol_01.preOrden()
arbol_01.postOrden()
print()

# 0 2 9 3 6 1 5 8 7 4
arbol_02 = Arboles(0)
arbol_02.adicionarDato(2)
arbol_02.adicionarDato(9)
arbol_02.adicionarDato(3)
arbol_02.adicionarDato(6)
arbol_02.adicionarDato(1)
arbol_02.adicionarDato(5)
arbol_02.adicionarDato(8)
arbol_02.adicionarDato(7)
arbol_02.adicionarDato(4)
arbol_02.inOrden()
arbol_02.preOrden()
arbol_02.postOrden()

# Buscar datos
print(arbol_01.buscar(7)) # Sí existe
print(arbol_01.buscar(12)) # No existe

print(bool(arbol_01.buscar(7))) # Sí existe
print(bool(arbol_01.buscar(12))) # No existe
