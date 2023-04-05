class Node():

	def __init__(self, valor):
		self.anterior  = None
		self.dato      = valor
		self.siguiente = None


class ListaDoEnlazada:

	def __init__(self):
		self.raiz = None
		self.cola = None

	def insertarAlFinal(self, nuevo_nodo):
		if self.raiz is not None:
			ultimo_nodo = self.raiz
			while ultimo_nodo.siguiente != None:
				ultimo_nodo = ultimo_nodo.siguiente

			nuevo_nodo.anterior   = ultimo_nodo
			ultimo_nodo.siguiente = nuevo_nodo
			self.cola 			  = nuevo_nodo
		else:
			self.raiz = nuevo_nodo
			self.cola = nuevo_nodo

	def imprimirIAD(self):
		print("IMPRIMIR DE IZQUIERDA A DERECHA")
		nodo_tmp = self.raiz
		print(" Null " , end=" <- ")
		while nodo_tmp != None:
			print(nodo_tmp.dato, end=" - ")
			nodo_tmp = nodo_tmp.siguiente
		print("> Null ")

	def imprimirDAI(self):
		print("IMPRIMIR DE DERECHA A IZQUIERDA")
		nodo_tmp = self.cola
		print(" Null " , end=" <- ")
		while nodo_tmp != None:
			print(nodo_tmp.dato, end=" - ")
			nodo_tmp = nodo_tmp.anterior
		print("> Null  ")

ld = ListaDoEnlazada()
n1 = Node("a")
n2 = Node("c")
n3 = Node("b")
ld.insertarAlFinal(n1)
ld.insertarAlFinal(n2)
ld.insertarAlFinal(n3)
ld.imprimirIAD()
ld.imprimirDAI()