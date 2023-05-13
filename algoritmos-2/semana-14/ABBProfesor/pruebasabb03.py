from arboles2023 import ArbolBinarioBusqueda
#Creacion de instancia
arbol01 = ArbolBinarioBusqueda()
#Adicion de valores
arbol01.insertar(40)
arbol01.insertar(20)
arbol01.insertar(60)
arbol01.insertar(10)
arbol01.insertar(30)
arbol01.insertar(50)
arbol01.insertar(70)
arbol01.insertar(45)
arbol01.insertar(55)
arbol01.insertar(54)
arbol01.insertar(75)


print("Arbol: ",arbol01)
print("En Orden:",arbol01.enOrden())
#Eliminación
print("Eliminacion 01:",arbol01.eliminar(30))
print("Arbol: ",arbol01)
print("En Orden:",arbol01.enOrden())
print("Eliminacion 02:",arbol01.eliminar(60))
print("Arbol: ",arbol01)
print("En Orden:",arbol01.enOrden())
print("Eliminacion 03:",arbol01.eliminar(70))
print("Arbol: ",arbol01)
print("En Orden:",arbol01.enOrden())

