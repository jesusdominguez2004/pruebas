from multilista2023 import *

#Creacion instancia
lista_01 = Multilista()

#Adicion elementos principal
lista_01.adicionarPrincipal(1)
lista_01.adicionarPrincipal(2)
lista_01.adicionarPrincipal(3)
lista_01.adicionarPrincipal(4)
lista_01.adicionarPrincipal(5)
print("Lista:",lista_01)
print("Lista Longitud:",lista_01.longitud())

#Adicion elementos secundaria
print("Adicion 1:",lista_01.adicionarSecundaria(8,10))
print("Adicion 2:",lista_01.adicionarSecundaria(4,15))
print("Adicion 2:",lista_01.adicionarSecundaria(1,100))

#Ver elementos secundaria
print("Buscar 01:",lista_01.verSecundaria(8))
print("Buscar 02:",lista_01.verSecundaria(4))
print("Buscar 03:",lista_01.verSecundaria(1))

