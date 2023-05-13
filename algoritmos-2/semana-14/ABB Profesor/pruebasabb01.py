from arboles2023 import ArbolBinarioBusqueda
#Creacion de instancia
arbol01 = ArbolBinarioBusqueda()
print("Arbol: ",arbol01)
print("Arbol Vacio: ",arbol01.estaVacio())
#Adicion de valores
arbol01.insertar(55)
arbol01.insertar(30)
arbol01.insertar(4)
arbol01.insertar(41)
arbol01.insertar(75)
arbol01.insertar(85)
print("Arbol: ",arbol01)
print("Arbol Vacio: ",arbol01.estaVacio())
print("En Orden:",arbol01.enOrden())