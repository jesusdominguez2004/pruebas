from arboles2023 import ArbolBinarioBusqueda
#Creacion de instancia
arbol01 = ArbolBinarioBusqueda()
#Adicion de valores
arbol01.insertar(5)
arbol01.insertar(4)
arbol01.insertar(1)
arbol01.insertar(3)
arbol01.insertar(7)
arbol01.insertar(6)
arbol01.insertar(9)
arbol01.insertar(8)
arbol01.insertar(10)
print("Arbol: ",arbol01)
print("En Orden:",arbol01.enOrden())
#Busqueda
print("Búsqueda 01:",arbol01.buscar(9))
print("Búsqueda 02:",arbol01.buscar(5))
print("Búsqueda 03:",arbol01.buscar(20))