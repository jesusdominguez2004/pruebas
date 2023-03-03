from multilista2023 import *

#Creacion instancia
lista_01 = Multilista()
print("Lista:",lista_01)
print("Esta Vacia:",lista_01.estaVacia())

#Adicion elementos
print("Ingreso 01")
lista_01.adicionarPrincipal(1)
print("Lista:",lista_01)
print("Ingreso 02")
lista_01.adicionarPrincipal(2)
print("Lista:",lista_01)
print("Ingreso 03")
lista_01.adicionarPrincipal(3)
print("Lista:",lista_01)
print("Lista Longitud:",lista_01.longitud())
print("Esta Vacia:",lista_01.estaVacia())

#Buscar elementos
print("Buscar 01:",lista_01.buscarPrincipal(5))
print("Buscar 02:",lista_01.buscarPrincipal(1))

