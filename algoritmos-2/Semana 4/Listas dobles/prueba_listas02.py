from listas_2022 import *

lista_02 = ListaSimple()
lista_02.adicionarAlInicio(10)
lista_02.adicionarAlInicio(20)
lista_02.adicionarAlInicio(30)
lista_02.adicionarAlInicio(40)
lista_02.adicionarAlInicio(50)
lista_02.adicionarAlInicio(60)
print("Lista 02:", lista_02)
#Buscar por posición
try:
    print("Posicion 01:",lista_02.buscarPosicion(-1))
except Exception as e:
    print(e)
print("Posicion 02:",lista_02.buscarPosicion(10))
print("Posicion 03:",lista_02.buscarPosicion(3))

#Eliminar
print("Eliminar 01:",lista_02.eliminarInfo(100))
print("Lista 02:", lista_02)
print("Eliminar 02:",lista_02.eliminarInfo(40))
print("Lista 02:", lista_02)
print("Eliminar 03:",lista_02.eliminarInfo(10))
print("Lista 02:", lista_02)
print("Eliminar 04:",lista_02.eliminarInfo(60))
print("Lista 02:", lista_02)

